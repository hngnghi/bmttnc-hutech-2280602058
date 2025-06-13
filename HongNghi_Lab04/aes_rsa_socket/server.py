from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

# Generate RSA key pair
server_key = RSA.generate(2048)

# List of connected clients
clients = []

# Function to encrypt message
def encrypt_message(key, message):
    # Create an AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC)
    # Pad the message to be a multiple of AES block size, encode to bytes, then encrypt
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    # Return the initialization vector (IV) and the ciphertext
    return cipher.iv + ciphertext

# Function to decrypt message
def decrypt_message(key, encrypted_message):
    # Extract the initialization vector (IV) from the beginning of the encrypted message
    iv = encrypted_message[:AES.block_size]
    # Extract the actual ciphertext after the IV
    ciphertext = encrypted_message[AES.block_size:]
    # Create a new AES cipher object with the key, CBC mode, and the extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the ciphertext, unpad it, and then decode it back to a string
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Function to handle individual client connections
def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")

    # Send server's public key to the client for secure key exchange
    # The public key is exported in PEM format
    client_socket.send(server_key.publickey().export_key(format='PEM'))

    # Receive the client's public key
    # RSA.import_key is used to parse the received key data
    client_received_key = RSA.import_key(client_socket.recv(2048))

    # Generate a random AES key for symmetric message encryption
    aes_key = get_random_bytes(16) # 128-bit key for AES

    # Encrypt the generated AES key using the client's public RSA key
    # PKCS1_OAEP is a standard for RSA encryption that adds padding for security
    cipher_rsa = PKCS1_OAEP.new(client_received_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    # Send the encrypted AES key to the client
    client_socket.send(encrypted_aes_key)

    # Add the connected client's socket and their AES key to the global list of clients
    clients.append((client_socket, aes_key))

    # Loop to continuously receive and forward messages from this client
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            # If no data is received, it means the client has disconnected
            if not encrypted_message:
                break # Exit the loop and handle disconnection

            # Decrypt the received message using the AES key exchanged with this client
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print(f"Received from {client_address}: {decrypted_message}")

            # If the client sends "exit", break the loop to close their connection
            if decrypted_message == "exit":
                break

            # Forward the decrypted message to all other connected clients
            # Each message is re-encrypted with the recipient's specific AES key
            for client_entry, key_entry in clients:
                if client_entry != client_socket: # Don't send the message back to the sender
                    encrypted = encrypt_message(key_entry, decrypted_message)
                    client_entry.send(encrypted)
        except Exception as e:
            # Catch any exceptions during communication (e.g., connection reset)
            print(f"Error handling client {client_address}: {e}")
            break # Exit the loop on error

    # Remove the client from the list once the loop breaks (connection closed or exited)
    clients.remove((client_socket, aes_key))
    # Close the client socket
    client_socket.close()
    print(f"Connection with {client_address} closed")

# Main loop to accept new client connections
while True:
    # Accept a new incoming connection
    client_socket, client_address = server_socket.accept()
    # Create a new thread to handle this client, so the server can accept more connections
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    # Start the thread
    client_thread.start()

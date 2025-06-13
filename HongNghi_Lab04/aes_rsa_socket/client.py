from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

# Initialize client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(('localhost', 12345))
except ConnectionRefusedError:
    print("Connection refused. Make sure the server is running on localhost:12345.")
    exit() # Exit if connection cannot be established

# Generate RSA key pair for the client
client_key = RSA.generate(2048)

# Receive server's public key for secure communication
try:
    server_public_key_pem = client_socket.recv(2048)
    server_public_key = RSA.import_key(server_public_key_pem)
except Exception as e:
    print(f"Error receiving server's public key: {e}")
    client_socket.close()
    exit()

# Send client's public key to the server
client_socket.send(client_key.publickey().export_key(format='PEM'))

# Receive the encrypted AES key from the server
try:
    encrypted_aes_key = client_socket.recv(2048)
except Exception as e:
    print(f"Error receiving encrypted AES key: {e}")
    client_socket.close()
    exit()

# Decrypt the AES key using the client's private RSA key
try:
    cipher_rsa = PKCS1_OAEP.new(client_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)
except Exception as e:
    print(f"Error decrypting AES key: {e}")
    client_socket.close()
    exit()

# Function to encrypt a message using AES
def encrypt_message(key, message):
    """
    Encrypts a message using AES in CBC mode.
    Args:
        key (bytes): The AES symmetric key.
        message (str): The plaintext message to encrypt.
    Returns:
        bytes: The IV concatenated with the ciphertext.
    """
    cipher = AES.new(key, AES.MODE_CBC)
    # Pad the message to a multiple of AES block size, encode to bytes, then encrypt
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext # Return IV + ciphertext

# Function to decrypt an AES encrypted message
def decrypt_message(key, encrypted_message):
    """
    Decrypts a message encrypted with AES in CBC mode.
    Args:
        key (bytes): The AES symmetric key.
        encrypted_message (bytes): The IV concatenated with the ciphertext.
    Returns:
        str: The decrypted plaintext message.
    """
    # Extract the initialization vector (IV) from the beginning
    iv = encrypted_message[:AES.block_size]
    # Extract the actual ciphertext
    ciphertext = encrypted_message[AES.block_size:]
    # Create a new AES cipher object with the key, CBC mode, and the extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the ciphertext, unpad it, and decode to string
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Function to receive messages from the server in a separate thread
def receive_messages():
    """
    Continuously receives and decrypts messages from the server.
    Runs in a separate thread.
    """
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message: # If no data, server disconnected
                print("Server disconnected.")
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print("Received:", decrypted_message)
        except OSError as e: # Handle connection errors (e.g., socket closed)
            print(f"Connection error while receiving: {e}")
            break
        except Exception as e: # Catch any other unexpected errors
            print(f"An unexpected error occurred while receiving: {e}")
            break

# Start the receiving thread to listen for incoming messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True # Allow main program to exit even if thread is running
receive_thread.start()

# Main loop for sending messages from the client
while True:
    try:
        message = input("Enter message ('exit' to quit): ")
        encrypted_message = encrypt_message(aes_key, message)
        client_socket.send(encrypted_message)
        if message.lower() == "exit": # Use .lower() for case-insensitive check
            break
    except OSError as e: # Handle connection errors during sending
        print(f"Connection error while sending: {e}")
        break
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred while sending: {e}")
        break

# Close the client socket when done (after 'exit' or error)
client_socket.close()
print("Client connection closed.")

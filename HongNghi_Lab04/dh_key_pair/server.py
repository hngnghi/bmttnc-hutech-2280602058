from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend # Recommended for backend selection

def generate_dh_parameters():
    """
    Generates Diffie-Hellman parameters.
    These parameters (p and g) are shared between parties to establish a shared secret.
    We use a generator of 2 and a key size of 2048 bits for security.
    """
    print("Đang tạo tham số Diffie-Hellman...") # Creating Diffie-Hellman parameters...
    # Generate parameters with a specific generator (g) and key size
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    print("Đã tạo tham số Diffie-Hellman thành công.") # Diffie-Hellman parameters created successfully.
    return parameters

def generate_server_key_pair(parameters):
    """
    Generates the server's Diffie-Hellman private and public key pair
    using the provided parameters.
    Args:
        parameters: The Diffie-Hellman parameters (p and g).
    Returns:
        tuple: A tuple containing the private key and the public key.
    """
    print("Đang tạo cặp khóa Diffie-Hellman của máy chủ...") # Creating server's Diffie-Hellman key pair...
    # Generate the private key using the parameters
    private_key = parameters.generate_private_key()
    # Derive the public key from the private key
    public_key = private_key.public_key()
    print("Đã tạo cặp khóa máy chủ thành công.") # Server key pair created successfully.
    return private_key, public_key

def main():
    """
    Main function to generate Diffie-Hellman parameters and server's key pair,
    then save the public key to a file.
    """
    # 1. Generate Diffie-Hellman parameters
    parameters = generate_dh_parameters()

    # 2. Generate server's private and public key pair using the parameters
    private_key, public_key = generate_server_key_pair(parameters)

    # 3. Save the server's public key to a PEM file
    # This public key will be shared with clients.
    try:
        with open("server_public_key.pem", "wb") as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
        print("Khóa công khai của máy chủ đã được lưu vào 'server_public_key.pem'") # Server public key saved to 'server_public_key.pem'
    except IOError as e:
        print(f"Lỗi khi lưu khóa công khai: {e}") # Error saving public key: {e}
    except Exception as e:
        print(f"Đã xảy ra lỗi không mong muốn: {e}") # An unexpected error occurred: {e}

if __name__ == "__main__":
    main()
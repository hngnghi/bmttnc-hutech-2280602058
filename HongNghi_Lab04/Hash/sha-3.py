from Crypto.Hash import SHA3_256

def sha3(message):
    # Initialize a SHA3-256 hash object
    sha3_hash = SHA3_256.new()
    # Update the hash object with the message (message should be bytes)
    sha3_hash.update(message)
    # Return the digest (hash value)
    return sha3_hash.digest()

def main():
    # Get text input from the user and encode it to UTF-8 bytes
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    # Calculate the SHA3 hash of the text
    hashed_text = sha3(text)

    # Print the original input text (decoded for readability)
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    # Print the SHA3 hash value in hexadecimal format
    print("SHA-3 Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()
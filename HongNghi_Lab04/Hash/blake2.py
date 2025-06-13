import hashlib

def blake2(message):
    # Initialize a BLAKE2b hash object with a digest size of 64 bytes (512 bits)
    blake2_hash = hashlib.blake2b(digest_size=64)
    # Update the hash object with the message (message should be bytes)
    blake2_hash.update(message)
    # Return the digest (hash value)
    return blake2_hash.digest()

def main():
    # Get text input from the user and encode it to UTF-8 bytes
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    # Calculate the BLAKE2 hash of the text
    hashed_text = blake2(text)

    # Print the original input text (decoded for readability)
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    # Print the BLAKE2 hash value in hexadecimal format
    print("BLAKE2 Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()
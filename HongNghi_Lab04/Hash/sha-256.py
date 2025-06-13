import hashlib

def calculate_sha256_hash(data):
    # Initialize a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Encode the input data to bytes and update the hash object
    sha256_hash.update(data.encode('utf-8'))
    # Return the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

# Get input data from the user
data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")
# Calculate the SHA-256 hash
hash_value = calculate_sha256_hash(data_to_hash)
# Print the original data and its SHA-256 hash value
print("Giá trị hash SHA-256:", hash_value)
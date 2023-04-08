import os
from Crypto.PublicKey import RSA # pip install pycryptodome, not crypto
from Crypto.Cipher import PKCS1_OAEP

def generate_keys():
    # Generate RSA keys with 2048 bits
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open('private_key.pem', 'wb') as f:
        f.write(private_key)
    with open('public_key.pem', 'wb') as f:
        f.write(public_key)

def read_keys():
    # Read RSA keys from files
    with open('private_key.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())
    with open('public_key.pem', 'rb') as f:
        public_key = RSA.import_key(f.read())
    return private_key, public_key

def encrypt_file(input_file_path, output_file_path, public_key, chunk_size=214):
    # Encrypt file using RSA encryption
    cipher = PKCS1_OAEP.new(public_key)
    with open(input_file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            while True:
                chunk = f_in.read(chunk_size)
                if len(chunk) == 0:
                    break
                encrypted_chunk = cipher.encrypt(chunk)
                f_out.write(encrypted_chunk)

def decrypt_file(input_file_path, output_file_path, private_key, chunk_size=256):
    # Decrypt file using RSA decryption
    cipher = PKCS1_OAEP.new(private_key)
    with open(input_file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            while True:
                chunk = f_in.read(chunk_size)
                if len(chunk) == 0:
                    break
                decrypted_chunk = cipher.decrypt(chunk)
                f_out.write(decrypted_chunk)

# Generate keys if they do not exist
if not os.path.exists('private_key.pem') or not os.path.exists('public_key.pem'):
    generate_keys()

# Read RSA keys
private_key, public_key = read_keys()

# Encrypt file
input_file_path = 'plaintext.txt'
output_file_path = 'ciphertext.txt'
encrypt_file(input_file_path, output_file_path, public_key)

# Decrypt file
input_file_path = 'ciphertext.txt'
output_file_path = 'decrypted_plaintext.txt'
try:
    decrypt_file(input_file_path, output_file_path, private_key)
except ValueError as e:
    print(f"Error: {e}\nAre you sure you're using the correct key?")

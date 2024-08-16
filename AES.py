from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import base64

def encrypt_message(message, password):
    # Generate a random 16-byte salt
    salt = os.urandom(16)

    # Derive a 32-byte key from the password using PBKDF2HMAC
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Generate a random 16-byte initialization vector (IV)
    iv = os.urandom(16)

    # Create a Cipher object using the AES algorithm in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Pad the message to be a multiple of the block size (16 bytes)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()

    # Encrypt the padded message
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()

    # Concatenate salt, IV, and ciphertext for storage/transmission
    encrypted_message = base64.b64encode(salt + iv + ciphertext).decode()

    return encrypted_message

# Example usage
message = "This is a secret message."
password = "strongpassword123"
encrypted = encrypt_message(message, password)
print("Encrypted message:", encrypted)
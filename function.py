import string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import base64

# Generate a random 16-byte initialization vector (IV) for AES
iv = os.urandom(16)
# Use hardcoded password to generate an AES key and for decryption
password = ">hA&52M2£5-0-aUx'fj/"

#* ---------------------------------------------------------------------------- #
#*                            Cipher Algorithms                                 #
#* ---------------------------------------------------------------------------- #

def ceasarEncrypt(message, key):
    alphabet = string.ascii_lowercase # The letters "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ""

    for c in message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + int(key)) % 26
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c
    return encrypted_message

def ceasarDecrypt(message, key):
    alphabet = string.ascii_lowercase # The letters "abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ""

    for c in message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - int(key)) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    return decrypted_message

def ceasarBruteforce(message):
    alphabet = string.ascii_lowercase # The letters "abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ""

    for i in range (1,26):
        for c in message:
            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - i) % 26
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message += c
        decrypted_message += "<br>"
    return decrypted_message

def aesEncrypt(message):
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

def aesDecrypt(message):
    # Decode the base64 encoded message
    encrypted_data = base64.b64decode(message)

    # Extract the salt, IV, and ciphertext from the encrypted data
    salt = encrypted_data[:16]
    ciphertext = encrypted_data[32:]

    # Derive the key from the password using the same method as in encryption
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Create a Cipher object using the AES algorithm in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding from the decrypted message
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()

    return message.decode()

def zigzagEncrypt(message, key):
    message = str(message)
    key = int(key)
    if(key < 2):
        # throw an error
        raise Exception("Rail fence encryption doesn't support less than 2 rows. <br> <a href='/'>Go Back</a>")
    # Create a matrix to store the rail fence pattern
    rail = [['\n' for _ in range(len(message))] for _ in range(key)]

    # Initialize variables to determine the direction of movement
    direction_down = False
    row, col = 0, 0

    # Fill the rail matrix with the characters of the message
    for char in message:
        # Change direction when reaching the top or bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        # Place the character in the rail matrix
        rail[row][col] = char
        col += 1

        # Move to the next row
        row += 1 if direction_down else -1

    # Construct the encrypted text by reading the matrix row by row
    encrypted_text = []
    for i in range(key):
        for j in range(len(message)):
            if rail[i][j] != '\n':
                encrypted_text.append(rail[i][j])

    return ''.join(encrypted_text)

def zigzagDecrypt(message, key):
    message = str(message)
    key = int(key)
    if(key < 2):
        # throw an error
        raise Exception("Rail fence encryption doesn't support less than 2 rows. <br> <a href='/'>Go Back</a>")
    # Create a matrix to store the rail fence pattern
    rail = [['\n' for _ in range(len(message))] for _ in range(key)]

    # Initialize variables to determine the direction of movement
    direction_down = None
    row, col = 0, 0

    # Mark the positions in the matrix where the characters will be placed
    for i in range(len(message)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        # Place a marker in the rail matrix
        rail[row][col] = '*'
        col += 1

        # Move to the next row
        row += 1 if direction_down else -1

    # Fill the rail matrix with the characters of the message
    index = 0
    for i in range(key):
        for j in range(len(message)):
            if rail[i][j] == '*' and index < len(message):
                rail[i][j] = message[index]
                index += 1

    # Read the matrix in a zigzag manner to construct the decrypted text
    result = []
    row, col = 0, 0
    for i in range(len(message)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        # Collect the characters from the rail matrix
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        # Move to the next row
        row += 1 if direction_down else -1

    return ''.join(result)

def zigzagBruteforce(message):
    possible_plaintexts = {}
    for key in range(2, len(message) + 1):
        decrypted_text = zigzagDecrypt(message, key)
        possible_plaintexts[key] = decrypted_text

    return possible_plaintexts

#* ---------------------------------------------------------------------------- #
#*                            Form Data Manipulation                            #
#* ---------------------------------------------------------------------------- #


def retrieveFormData(form_data: dict):
    text: string = form_data["text"].lower()
    step: int = form_data["step"]
    direction: string = form_data["direction"]

    if(direction != "decrypt" and step is None):
        # throw an error
        raise Exception("Developer error: encryption in bruteforce mode is not supported.")

    return text, step, direction
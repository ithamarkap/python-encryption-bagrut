import string

# functions

def ceasarEncrypt(message, key):
    alphabet = string.ascii_lowercase # The letters "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ""

    for c in message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + key) % 26
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
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    return decrypted_message    

def atbashCrypt(message):
    # This function uses a lookup_table to replace the letters for the cipher
    lookup_table = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
                    'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
                    'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
                    'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
                    'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

    cipher = ''
    for letter in message:
        # checks if the string is an alphabetic letter
        if (letter.isalpha()):
            # adds the letter from the lookup table
            cipher += lookup_table[letter]
        else:
            # if the string is not an alphabetic letter, add a space instead
            cipher += ' '
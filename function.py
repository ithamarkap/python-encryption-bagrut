import string

#* ---------------------------------------------------------------------------- #
#*                            Cipher Algorithms                             #
#* ---------------------------------------------------------------------------- #

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

# TODO: implement Atbash
def atbashEncrypt(message):
    return message[::-1]


#* ---------------------------------------------------------------------------- #
#*                            Form Data Manipulation                            #
#* ---------------------------------------------------------------------------- #


def retrieveFormData(form_data: dict):
    text: string = form_data["text"].lower()
    step: int = form_data["step"]
    direction: string = form_data["direction"]

    if(type(step) != int):
        try:
            step = int(step)
        except ValueError:
            raise Exception("Step must be an integer")

    if(direction != "encrypt" and direction != "decrypt"):
        # throw an error
        raise Exception("Developer error: direction must be 'encrypt' or 'decrypt'")

    return text, step, direction
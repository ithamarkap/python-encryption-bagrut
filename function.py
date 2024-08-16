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
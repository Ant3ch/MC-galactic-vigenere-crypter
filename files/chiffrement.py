import random


def chiffrage_minecraftien(message: str):
    alphabet, reverse_alphabet = get_minecraftien_alphabet()
    message_chiffree = ""
    message = message.upper()
    for letter in message:
        if letter in alphabet:
            letter = alphabet[letter]
            message_chiffree += letter

    return message_chiffree


def dechiffrage_minecraftien(message: str):
    alphabet, reverse_alphabet = get_minecraftien_alphabet()
    message = message.upper()
    message_dechifree = ""
    once = 1
    for letter in message:

        # double characters correction

        indx = message.index(letter)
        if message[indx] == "!" and message[indx + 1] == "¡":
            message_dechifree += reverse_alphabet["!¡"]

        if message[indx] == "|" and message[indx + 1] == "|" and once == 1:
            message_dechifree += reverse_alphabet[message[indx] + message[indx]]
            once -= 1

        if letter in reverse_alphabet:
            letter = reverse_alphabet[letter]
            message_dechifree += letter

    return message_dechifree


def chiffrage_cesar(message: str, n: int):
    message_encrypted = ""
    message_ints = []
    encrypted_ints = []
    for caracters in message:
        message_ints.append(ord(caracters))

    for ords in message_ints:
        ords += n
        encrypted_ints.append(ords)

    for encrypted_integer in encrypted_ints:
        message_encrypted += chr(encrypted_integer)
    return message_encrypted


def dechiffrage_cesar(message: str, n: int):
    decrypted_message = ""
    encrypted_ints = []
    decrypted_ints = []
    for caracters in message:
        encrypted_ints.append(ord(caracters))

    for ords in encrypted_ints:
        new_ord = ords - n
        if new_ord < 0:
            break
        else:
            decrypted_ints.append(chr(new_ord))

    for decrypted_int in decrypted_ints:
        decrypted_message += decrypted_int

    return decrypted_message


def brutforceCesar(message: str):
    liste = []
    for i in range(1, 255):
        brutforced_message = dechiffrage_cesar(message, i)
        liste.append(brutforced_message)

    for value in liste:
        if value == None or value == " " or value == "":
            liste.remove(liste[liste.index(value)])
        if value == message:
            print("hello")

    return liste


def get_ascii_alphabet():
    alphga = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]
    result = []
    for alphgas in alphga:
        first = alphgas
        alphgas = ord(alphgas)
        result.append(f"{first}>{alphgas}")
    return result


def get_minecraftien_alphabet():
    alphabet = {"A": "ᔑ", "B": "ʖ", "C": "ᓵ", "D": "↸", "E": "ᒷ", "F": "⎓", "G": "⊣", "H": "⍑", "I": "╎", "J": "⋮",
                "K": "ꖌ", "L": "ꖎ", "M": "ᒲ", "N": "リ", "O": "𝙹", "P": "!¡", "Q": "ᑑ", "R": "∷", "S": "ᓭ", "T": "ℸ",
                "U": "⚍", "V": "⍊", "W": "∴", "X": "̇/", "Y": "||", "Z": "⨅", " ": " ", "?": "?", "!": "!", ".": ".",
                ",": ","}

    reverse_alphabet = {v: k for k, v in alphabet.items()}
    return alphabet, reverse_alphabet


def create_random_password(lenght: int) -> str:
    phrase_random = []
    message = ""
    for i in range(lenght):
        phrase_random.append(chr(random.randint(65, 90)))

    for i in phrase_random:
        message += i
    return message


def ignore_characters_vignere() -> dict:
    no_change_character = {
        "caract": [" ", ",", ".", "?", ":", "'", ";", "!", "%", "*", "$", "=", "+", "-", "{", "}", "[", "]", "^", "/",
                   '"', "&", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], "ords": []}
    for i in range(len(no_change_character["caract"])):
        no_change_character["ords"].append(1000 + i)
    return no_change_character


def chiffrage_vigenere(User_text: str, input_key: str) -> str:
    encrypted_message = ""
    User_text = User_text.upper()
    text_character = []
    key = []

    ignore_character = ignore_characters_vignere()

    # turn user text input into list, same process for the key
    for characters in User_text:
        text_character.append(characters)

    for characters in input_key:
        key.append(characters)

    # get the key same size
    while len(key) < len(User_text):
        for i in range(len(key)):
            if len(key) < len(User_text):
                key.append(key[i])

    if len(key) > len(User_text):
        while len(key) != len(User_text):
            key.pop(len(key) - 1)

    # turn the key in to ord
    for characters in key:
        indx = key.index(characters)
        key[indx] = ord(characters) - 65

    for characters in text_character:
        indx = text_character.index(characters)

        if characters not in ignore_character["caract"]:  # to prevent from ignored character
            text_character[indx] = ord(characters) - 65 + key[indx]
        else:
            # if it's an ignored character you gonna attribute a a value based on the character(that value is choosen !)
            caracter_indx = ignore_character["caract"].index(characters)
            text_character[indx] = ignore_character["ords"][caracter_indx]

    # converting into character
    for characters in text_character:
        if characters not in ignore_character["ords"]:  # same as before
            encrypted_message += chr(characters % 95 + 65)
        else:
            ord_index = ignore_character["ords"].index(characters)
            encrypted_message += ignore_character["caract"][ord_index]
    return encrypted_message


def dechiffrage_vigenere(message: str, cle: str):
    decrypted_message = ""
    message = message.upper()
    messages = []
    key = []

    no_change_character = ignore_characters_vignere()

    # convert to list
    for letter in message:
        messages.append(letter)

    print(messages)

    for letter in cle:
        key.append(letter)
    # get the key same size
    while len(key) < len(message):
        for i in range(len(key)):
            if len(key) < len(message):
                key.append(key[i])

    if len(key) > len(message):
        while len(key) != len(message):
            key.pop(len(key) - 1)

    # convert into ascii

    for letter in key:
        indx = key.index(letter)
        key[indx] = ord(letter) - 65
        key[indx] = 26 - key[indx]

    # string to number
    for letter in messages:
        indx = messages.index(letter)
        if letter not in no_change_character["caract"]:
            messages[indx] = ord(letter) - 65 + key[indx]  # calc with key
        else:
            caracter_indx = no_change_character["caract"].index(letter)
            messages[indx] = no_change_character["ords"][caracter_indx]
    print(messages)

    # number to string
    for letter in messages:
        indx = messages.index(letter)
        if letter not in no_change_character["ords"]:
            decrypted_message += chr(letter % 26 + 65)
        else:

            ord_index = no_change_character["ords"].index(letter)
            decrypted_message += no_change_character["caract"][ord_index]

    return decrypted_message


a = chiffrage_vigenere("QSD", "ABC")
a = chiffrage_minecraftien(a)

a = dechiffrage_minecraftien(a)
B = dechiffrage_vigenere(a, "ABC")

print(a, B)

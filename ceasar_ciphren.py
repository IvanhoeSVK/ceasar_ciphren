import sys
import string

alphabet = list(string.ascii_lowercase)
encode_word = ""
decode_word = ""

def encode():
    global encode_word
    word = (input("Enter the word you want to encode: ")).lower().strip()
    while True:
        shift = input("Enter shift: ")
        if shift.isdigit():
            break
        else:
            print("Enter only number!\n")
            continue
    for letter in word:
        letter_index = alphabet.index(letter)
        new_index = letter_index + int(shift)
        if new_index >= 26:
            new_index %= 26
        encode_word += alphabet[new_index]
    print(f"Encode word is: {encode_word}\n")

def decode():
    global decode_word
    word = input("Enter word you want to decode: ").lower().strip()
    while True:
        shift = input("Enter shift: ")
        if shift.isdigit():
            break
        else:
            print("Enter only number!\n")
            continue
    for letter in word:
        letter_index = alphabet.index(letter)
        new_index = letter_index - int(shift)
        if new_index >= 26:
            new_index %= 26
        decode_word += alphabet[new_index]
    print(f"Decode word is : {decode_word}\n")
    

print("Welcome To Caesar Ciphren!\n")

while True:
    while True:
        action = input("""What do you want?
                    1 - encode
                    2 - decode\n""")
        if action in ["1", "2"]:
            if action == "1":
                encode()
                break
            if action == "2":
                decode()
                break
        else:
            print("Enter only 1 or 2!")
            continue


    
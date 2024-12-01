import sys
import string

alphabet = list(string.ascii_lowercase)
encode_word = ""

word = (input("Enter the word you want to encode: ")).lower()
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
    encode_word += alphabet[new_index]
    print(encode_word)
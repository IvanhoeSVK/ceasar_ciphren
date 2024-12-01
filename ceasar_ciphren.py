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
    if new_index >= 26:
        new_index %= 26
    encode_word += alphabet[new_index]
print(f"Encode word is: {encode_word}")
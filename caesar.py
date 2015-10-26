# Caesar Cisper
# Based on inventwithpython

import pyperclip

message = raw_input('Please enter a message: ')

key = input('How many to move by: ')

mode = raw_input('encrypt or decrypt: ')

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = message.upper()

for symbols in message:
    if symbols in LETTERS:
        # get the encrupted number
        num = LETTERS.find(symbols)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]

    else:
        translated = translated + symbols


print(translated)

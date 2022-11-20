# Vigenere Cipher (Polyalphabetic Substitution Cipher)
#

import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    # This text can be downloaded from ...
    myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    myKey = "ASIMOV"
    myMode = 'encrypt' # set to either 'encrypt' or 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    
    print("%sed message:" % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clipboard.')


def encryptMessage(key, message):
    return translatedMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translatedMessage(key, message, 'decrypt')


def translatedMessage(key, message, mode):
    translated = [] # Stores the encrypted/decrypted message string

    keyIndex = 0
    key = key.upper()

    for symbol in message: # loop through each symbol in message
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting
            
            num %= len(LETTERS) # handle any wraparound

            # add the encrypted/decrypted symbol to the end of the translated:
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # Move to the next letter in the key.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # append the sumbol without encrypting/decrypting
            translated.append(symbol)
    
    return ''.join(translated)


# if vigenereCipher.py is run (instead of import as a module), call
# the main() function
if __name__ == '__main__':
    main()
        
        


    



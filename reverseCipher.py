#Reverse Cipher 


message = "Three can keep a secret, if two of them are dead."
translated = ''

i = len(message) - 1
while i >= 0:
    translated += message[i]
    i -= 1

print(translated)
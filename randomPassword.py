import random

def password():
    password = ""
    while len(password) < 20:
        randomSymbol = chr(random.randint(32, 91))
        if randomSymbol not in password:
            password += randomSymbol
    return password       
print(password())

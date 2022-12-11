import random
import pyperclip


def password():
    box = """"""
    while len(box) < 20:
        ran_symbol = chr(random.randint(32, 91))
        if ran_symbol not in box:
            box += ran_symbol
    print(box)
    pyperclip.copy(box)


password()

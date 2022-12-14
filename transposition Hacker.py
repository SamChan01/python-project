# Transpositon Cipher Hacker
#

import pyperclip, detectEnglish, transpositionDecrypt

def main():
    # You might want to copy & paste this text from the source code at
    # 
    myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print("Failed to hact encryption")
    else:
        print("Copying hacked message to clipboard:")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)


def hackTransposition(message):
    print("hacking...")

    # Python program can be stopped at any time bu pressing
    # Ctrl-C (on windows) or Ctrl-D(on macOS and Linux):
    print("(Press Ctrl-C (on windows) or Ctrl-D(on macOS and Linux) to quit at any time.)")

    # Brute-force by looping through every possible key:
    for key in range(1, len(message)):
        print("Trying key #%s..." % (key))

        decryptedText = transpositionDecrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            # Ask user if this is correct decryption
            print()
            print("Possible encryption hack: ")
            print("Key %s: %s" % (key, decryptedText[:100]))
            print()
            print("Enter D if done, anything else to continue hacking:")
            response = input('> ')

            if response.strip().upper().startswith("D"):
                return decryptedText
    
    return None

if __name__ == "__main__":
    main()


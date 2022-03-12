#!usr/bin/python3

import rsa
import os

os.system('clear')
print ("""
 █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗ 
██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗
███████║██║     ██████╔╝███████║███████║
██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║
██║  ██║███████╗██║     ██║  ██║██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝                     
===========+coded by ALPHA+=============
""")

import time
import sys

done = 'false'
#here is the animation
def animate():
    while done == 'false':
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

animate()
#long process here
done = 'false'      

def main():
    choice = int(input("1. Encryption\n2. Decryption\n3. Creators\n4. GitHub\nChoose (1,2,3,4): "))
    if choice == 1:
        print("--+Encryption+--")
        cipher_encryption()
    elif choice == 2:
        print("--+Decryption+--")
        cipher_decryption()
    elif choice == 3:
        print("--+Creators+--")
        credits()
    elif choice == 4:
        print("--+GitHub+--")
        github()
    else:
        print("Invalid Choice")

def cipher_encryption():
    message = input("Enter Message:")
    key = 47
    encryp_text = ""

    for i in range(len(message)):
        temp = ord(message[i]) + key
        if ord(message[i]) == 32:
            encryp_text += " "
        elif temp > 126:
            temp -= 94
            encryp_text += chr(temp)
        else:
            encryp_text += chr(temp)
        # if-else
    # for

    print("Encrypted Text: {}".format(encryp_text))

def cipher_decryption():
    message = input("Enter message: ")
    key = 47
    decryp_text = ""

    for i in range(len(message)):
        temp = ord(message[i]) - key
        if ord(message[i]) == 32:
            decryp_text += " "
        elif temp < 32:
            temp += 94
            decryp_text += chr(temp)
        else:
            decryp_text += chr(temp)
            # if-else
    # for

    print("Decrypted Text: {}".format(decryp_text))
    
def credits():
    os.system('clear') 
    message = print("OWNER: XML, CREDITS: BLACKHATPARROT")

def github():
        print("https://github.com/xmlalpha")  

if __name__ == "__main__":
    main()

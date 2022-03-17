from secrets import choice
import sys
import rsa
import os
from time import sleep

from time import sleep
import tqdm

for i in tqdm.tqdm(range(100)):
    sleep(0.1)
    

def main():
print("""
 █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗ 
██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗
███████║██║     ██████╔╝███████║███████║
██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║
██║  ██║███████╗██║     ██║  ██║██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝                     
===========+coded by ALPHA+=============""")

    choice = int(input("1. Encryption\n2. Decryption\n3. Creators\n4. \nChoose (1,2,3): "))
    if choice == 1:
        os.system('clear')
        print("""
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝""")
        sleep(5)
        cipher_encryption()
    elif choice == 2:
        os.system('clear')
        print("""
██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╔╝██║ ╚████║
╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝""")
        sleep(5)
        cipher_decryption()
    elif choice == 3:
        if choice == 3:
            os.system('clear')
            print("""
 ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ ███████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝███████╗
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗╚════██║
╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║███████║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝""")
        sleep(5)
        creators()
    else:
        print("Invalid Choice")


def cipher_encryption():
    if choice == 1:
        os.system('clear')
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
    if choice == 2:
        os.system('clear')
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
    
def creators():
        print("OWNER: XML")
        print("CREDITS: RadoslavAtanasov")

if __name__ == "__main__":
    main()

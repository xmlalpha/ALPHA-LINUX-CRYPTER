#!usr/bin/python3

import rsa
import os
from time import sleep
k='#'
j=0
k='#'
def fixed_space(i,array):
    g=(' '*len(str(len(array))))
    g=g.replace(' ','',len(str(int(i))))
    return g
def ani(i,array):
    global k
    #For accessing the global variables that are defined out of the function
    global j
    per=((i+1)*100)//len(array)
    #To calculate percentage of completion of loop
    c=per//5
    #Integer division (the value 5 decides the length of the bar)
    if c!=j:
    #When ever the values of these 2 variables change add one # to the global variable k
        k+='#'
    y='['+k+'                     '+']'
    #20 empty spaces (100/5) 
    y=y.replace(' ','',len(k))
    #To make the size of the bar fixed ever time the length of k increases one ' ' will be removed
    g=fixed_space(per,array)
    #To fix at the same position
    f=fixed_space(i,array)
    print('Loading : ',y,g+str(per)+'%',' ('+f+str(i+1)+' / '+str(len(array))+' ) ',end='\r')
    #That same '\r' to clear previous text
    j=c

array = range(100)
for i in array:
    ani(i,array)
    sleep(0.1)
    os.system("cls")


def main():
    print("""
 █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗ 
██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗
███████║██║     ██████╔╝███████║███████║
██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║
██║  ██║███████╗██║     ██║  ██║██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝                     
===========+coded by ALPHA+=============""")

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
    message = print("OWNER: XML, CREDITS: BLACKHATPARROT")

def github():
        print("https://github.com/xmlalpha")  

if __name__ == "__main__":
    main()

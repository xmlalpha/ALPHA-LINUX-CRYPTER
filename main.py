import rsa
import os

os.system('clear')
print ("""
   ▄████████  ▄█          ▄███████▄    ▄█    █▄       ▄████████ 
  ███    ███ ███         ███    ███   ███    ███     ███    ███ 
  ███    ███ ███         ███    ███   ███    ███     ███    ███ 
  ███    ███ ███         ███    ███  ▄███▄▄▄▄███▄▄   ███    ███ 
▀███████████ ███       ▀█████████▀  ▀▀███▀▀▀▀███▀  ▀███████████ 
  ███    ███ ███         ███          ███    ███     ███    ███ 
  ███    ███ ███▌    ▄   ███          ███    ███     ███    ███ 
  ███    █▀  █████▄▄██  ▄████▀        ███    █▀      ███    █▀  
             ▀                                                                      
=====================+coded by ALPHA+==========================
""")

print()
print("Loading...")
publicKey, privateKey = rsa.newkeys(4096)

message = input("Enter your text>")
print()
print()
encMessage = rsa.encrypt(message.encode(),
						publicKey)

print("original string>", message)
print()
print()
print("encrypted string>", encMessage)

decMessage = rsa.decrypt(encMessage, privateKey).decode()
print()
print()
print("decrypted string>", decMessage)
 

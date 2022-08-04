#!/usr/bin/env python3

import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = get_random_bytes(AES.block_size)

login_info = {
        "alice" : "97bf34d31a8710e6b1649fd33357f783",
        "bob" : "bbb2c5e63d2ef893106fdd0d797aa97a",
        "charlie" : "d8578edf8458ce06fbc5bb76a58c5ca4",
        "dan" : "857b2b431dcd8049ec5859c88f78e1a7",
        "eve" : "9039d6f4e642291c6074fc5812ab1cc7"}

def restrict():
    print("///////////////////////////////////////////////////////////////")
    print("/////////////////////// UNSECURE ACCESS ///////////////////////")
    print("///////////////////////////////////////////////////////////////")
    print("\n** ALL FILES ON THIS SERVER HAVE BEEN ENCRYPTED AS A PRECAUTION **\n")

def get_byte(string):
    x = 0
    for letter in string:
        x += ord(letter)
    return (x % 5) + 1


def login():
    print("Please login to download content")
    user = input("username: ")
    pswd = input('password: ')

    if user not in login_info.keys():
        print("Incorrect username...")
        return -1

    if hashlib.md5(pswd.encode()).hexdigest() == login_info[user]:
        return get_byte(pswd)

    print("Incorrect password...")
    return -1

def encrypt(mode_str, data):
    header = data[:0x4a]
    data = data[0x4a:]
    iv = get_random_bytes(AES.block_size)
    if mode_str == 1:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
    elif mode_str == 2:
        cipher = AES.new(key, AES.MODE_CFB, iv)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
    elif mode_str == 3:
        cipher = AES.new(key, AES.MODE_OFB, iv)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
    elif mode_str == 4:
        cipher = AES.new(key, AES.MODE_CTR, iv)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
    elif mode_str == 5:
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))

    output = header + ciphertext
    print(output.hex())

def menu(mode):
    print("\n**ACCESS GRANTED**\n")
    print("You are not authorized to download unencrypted content on this server.")
    while True:
        print("\nPlease select the file(s) you wish to download or type '0' to quit")
        print("The file will be encrypted and sent in hex format")
        print("----------------")
        print("0. exit")
        print("1. secrets.bmp")
        print("2. reveille.bmp")
        print("3. picture1.bmp")
        print("4. flag.bmp")

        choice = input("\nEnter file selection: ")[0]

        if choice == '0':
            print("Logging off...")
            return
        elif choice == '1':
            filename = 'secrets.bmp'
        elif choice == '2':
            filename = 'reveille.bmp'
        elif choice == '3':
            filename = 'picture1.bmp'
        elif choice == '4':
            filename = 'flag.bmp'
        else:
            print("Invalid input")
            continue
        
        file = open(filename, 'rb')
        data = file.read()
        encrypt(mode, data)


if __name__ == '__main__':
    restrict()
    result = login()

    if result != -1:
        menu(result)
    else:
        print("Session terminated")

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secrets import token_bytes

BLOCK_SIZE = 16

key = open('key.txt', 'rb').read()
signature = open('flag.txt', 'rb').read()
cipher = AES.new(key, AES.MODE_ECB)

print("Howdy!")
while True:
    print("Enter a message to encrypt")
    m = input("> ").encode('utf-8')
    print("Here is your encrypted message. We also added a signature to verify during decryption:")
    padded = pad(m+signature, BLOCK_SIZE)
    print(cipher.encrypt(padded).hex())


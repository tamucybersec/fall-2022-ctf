from secrets import token_bytes

KEY_LEN = 6

key = token_bytes(KEY_LEN)

flag = REDACTED

ct = b''
for i, c in enumerate(flag):
    ct += (key[i%KEY_LEN] ^ ord(c)).to_bytes(1, byteorder='big')

print(ct)

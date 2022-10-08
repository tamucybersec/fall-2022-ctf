from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes

p = remote("localhost", 8888)
p.recvuntil(b"n = ")
n = int(p.recvline().decode())
p.recvuntil(b"e = ")
e = int(p.recvline().decode())
p.recvuntil(b"d = ")
d = int(p.recvline().decode())
p.recvuntil(b"msg1 = ")
msg1 = int(p.recvline().decode())
p.sendline(str(pow(msg1, e, n)).encode())
p.recvuntil(b"ctxt1 = ")
ctxt1 = int(p.recvline().decode())
p.sendline(str(pow(ctxt1, d, n)).encode())
p.recvuntil(b"msg = ")
msg = p.recvline()[:-1]
p.sendline(str(pow(bytes_to_long(msg), e, n)).encode())
p.recvuntil(b"ctxt = ")
ctxt = int(p.recvline().decode())
print(long_to_bytes(pow(ctxt, d, n)).decode())

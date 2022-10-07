from pwn import *
from Crypto.Util.number import long_to_bytes

p = remote('localhost', 8000)

n = int(p.recvline().split(b' ')[2].strip(), 16)
e = int(p.recvline().split(b' ')[2].strip(), 16)

p.recvline()

flag_ct = int(p.recvline().split(b' ')[3].strip(), 16)

p.sendline(hex(pow(2, e, n) * flag_ct).encode())

p.recvline()

flag_pt = int(p.recvline().split(b' ')[-1].strip(), 16)

pt_inv = pow(2, -1, n)

print(long_to_bytes(flag_pt * pt_inv % n))

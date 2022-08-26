from pathlib import Path
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, inverse, GCD
from Crypto.Random.random import randint

def is_coprime(p, q):
    return GCD(p, q) == 1

flag = Path("flag.txt").read_text().strip().encode()
plaintext = bytes_to_long(flag)
p = getPrime(512)
q = getPrime(512)
n = p * q
phi = (p - 1) * (q - 1)

while True:
    d = randint(2, 1024)
    e = inverse(d, phi)
    if 1 < e < phi and is_coprime(e, phi):
        break

c = pow(plaintext, e, n)

print(f"N = {n}")
print(f"e = {e}")
print(f"c = {c}")

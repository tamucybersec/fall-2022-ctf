from Crypto.Util.number import getPrime, bytes_to_long
from math import sqrt, gcd
from random import randint

# nice
q = getPrime(420)

u = int(sqrt(q//2))
l = int(sqrt(q//4))

# Generate private key (f, g)
f = randint(2, u)
while True:
    g = randint(l, u)
    if gcd(f, q*g) == 1:
        break

h = (pow(f, -1, q) * g) % q

print("public key:")
print(f"q = {q}")
print(f"h = {h}")

# Encrypt the flag
flag = b"REDACTED"
r = randint(2, u)


assert bytes_to_long(flag) < u
e = (r*h + bytes_to_long(flag)) % q
print("encrypted flag:")
print(f"e = {e}")

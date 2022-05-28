from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long
from random import randint
from collections import namedtuple

# Defining some things to do EC math easier, shamelessly copy-pasted from cryptohack.org
Point = namedtuple("Point", "x y")

O = 'Origin'

def check_point(P: tuple):
    if P == O:
        return True
    else:
        return (P.y**2 - (P.x**3 + a*P.x + b)) % p == 0 and 0 <= P.x < p and 0 <= P.y < p


def point_inverse(P: tuple):
    if P == O:
        return P
    return Point(P.x, -P.y % p)

# returns the point P+Q
def point_addition(P: tuple, Q: tuple):
    # based of algo. in ICM
    if P == O:
        return Q
    elif Q == O:
        return P
    elif Q == point_inverse(P):
        return O
    else:
        if P == Q:
            lam = (3*P.x**2 + a)*inverse(2*P.y, p)
            lam %= p
        else:
            lam = (Q.y - P.y) * inverse((Q.x - P.x), p)
            lam %= p
    Rx = (lam**2 - P.x - Q.x) % p
    Ry = (lam*(P.x - Rx) - P.y) % p
    R = Point(Rx, Ry)
    assert check_point(R)
    return R

# returns the point nP
def double_and_add(P: tuple, n: int):
    # based of algo. in ICM
    Q = P
    R = O
    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q)
        Q = point_addition(Q, Q)
        n = n // 2
    assert check_point(R)
    return R

# Kudos if you know where these curve parameters are from
p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
a = 0
b = 7
n = 69420

G = Point(55066263022277343669578718895168534326250603453777594175500187360389116729240, 32670510020758816978083085130507043184471273380659243275938904335757337482424)

from ast import literal_eval as parse_tuple
from pwn import *

context.log_level = "debug"
io = remote("localhost", 7077)

d_B = randint(1, 69420)
B = double_and_add(G, d_B)
A = Point(*parse_tuple(io.recvline().decode()))
io.sendline(f"{B.x},{B.y}")
secret = long_to_bytes(double_and_add(A, d_B).x)
c = long_to_bytes(int(io.recvline().decode()))
flag = xor(secret, c)
print(flag)

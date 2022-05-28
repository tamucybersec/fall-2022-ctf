# DiffieCC

Take this, it's dangerous to go alone: [Wikipedia](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman)

Alls you got to do is successfully perform the key exchange with Alice and she will send you the encrypted flag!


Given: chall.py and a remote connection. Everything else is unknown to the solver

Setup instructions:
```sh
docker build --tag=diffiecc .
docker run --name diffiecc -d -p <port>:7077 diffiecc
```

Then you can connect to it on <port>:
```sh
nc localhost <port>
```

To clean up the docker images/containers after:
```sh
docker stop diffiecc
docker rm diffiecc
docker image rm diffiecc
```

## Solution
Reading from the provided link, all we need to do is compute the point d_B * Q_A, then take the x-coordinate to acquire the secret used to encrypt the flag. Note that the `*` isn't your everyday multiplication since we're dealiing with elliptic curves; if you google "double_and_add", the first Wikipedia page will tell you it does elliptic curve point multiplication, so we can just reuse the provided function to perform the operation. The relevant snippet is provided; see `solve.py` for the full script.

```python
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
```

Flag: `gigem{k3ys_exch4nged_fl4g_acqu1red}`

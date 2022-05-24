# DiffieCC

Take this, it's dangerous to go alone: [Wikipedia](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman)

Alls you got to do is successfully perform the key exchange with Alice and she will send you the encrypted flag!


Given: chall.py and a remote connection. Everything else is unknown to the solver

Setup instructions:
```sh
docker build --tag=diffiecc .
docker run --name diffiecc -p <port>:7077 diffiecc &
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


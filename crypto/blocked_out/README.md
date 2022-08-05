# Blocked Out

Oops, the server has blocked its users from downloading unencrypted content. Get on there and find a way to get the flag!

**Note: If you can find a way to make it harder please add to it or suggest something**

## Dev Notes

The user has access to `chall.py`

## Solution

There are 4 users available. All of them have weak md5 hashes that I was able to crack at crackstation.net. In the encrypt function there is multiple options for ciphers that are decided based on the return value of `get_byte()`. The weakest encryption available is `ECB`. Using that function, it is determined that `charlie` is the user needed to access the weak encryption scheme of `ECB`. `ECB` is weak because in data with lots of repetition, information can still be leaked. For a cool example lookup `ECB tux penguin`.

Once the data is exported with this user it can be decoded from hex and placed into a file. From there the file can be opened; revealing the flag. The script I used to automate the process of getting the file data is included.

```python
from pwn import *

p = remote('127.0.0.1', 8888)
#p = process('./chall.py')

p.recvuntil(b'username: ')
p.sendline(b'charlie')
p.recvuntil(b'password: ')
p.sendline(b'qwerty')
p.recvuntil(b'selection: ')
p.sendline(b'4')

file = p.recvuntil(b'\n\nPlease')
file = file[:-8]

header = file[:0x4a]
data = file[0x4a:]

f = open('flag.bmp', 'wb')
f.write(bytes.fromhex(header.decode('latin-1')))
f.write(bytes.fromhex(data.decode('latin-1')))
f.close()

exit()
```


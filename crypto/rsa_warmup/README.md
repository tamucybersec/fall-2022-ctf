# RSA Warmup

Respond to this RSA challenge with the right stuff to get the flag!

You might want these:

- [pow](https://docs.python.org/3/library/functions.html#pow)
- [bytes_to_long](https://pycryptodome.readthedocs.io/en/latest/src/util/util.html#Crypto.Util.number.bytes_to_long)
- [long_to_bytes](https://pycryptodome.readthedocs.io/en/latest/src/util/util.html#Crypto.Util.number.long_to_bytes)


## Dev
No files are given.
Set up the server with
```
make docker
make run
```

by default the server runs on port 8888 

To clean everything:
```
make clean
```

## Solution
See `solve.py` for the full solve.

Here's what you need to know:
```python
# encryption
ciphertext_as_int = pow(plaintext_as_int, e, n)
# decryption
plaintext_as_int = pow(ciphertext_as_int, d, n)

from Crypto.Util.number import bytes_to_long, long_to_bytes

# converting messages to and from integers
secret_message_as_int = bytes_to_long(b"attack at dawn!")
orignal_secret_message = long_to_bytes(secret_message_as_int)
```

Flag: `gigem{rs4_1s_fun!}`

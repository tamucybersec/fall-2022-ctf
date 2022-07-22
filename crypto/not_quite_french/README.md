# Not quite French

I saw a cipher online and tried to make my own version. There's no way my cipher has any weakness and you'll never get the flag!

## Solution
Looking at the source, it appears to rotate each of the first `key_len` bytes by the corresponding byte in the key, then if the plaintext is longer than the key, rotates the following values by the byte in the ciphertext at `i - key_len` where `i` is the index of the current byte.

First I reversed the first section using the flag format as a crib to get the key:
```py
alpha_num = "abcdefghijklmnopqrstuvwxyz1234567890_{}? "
alpha_len = len(alpha_num)
ct = 'ss9nw63du7fz1dgc}_ef1bfk{oln?les_1ttf5ds}e?tqa2reetxpsa4idy9p s3qqxmwh_265{48600ceh8e0hnghg8ynvxk6f0733225lc}7 x4{?eh2xrin9gyk}ick'
crib = 'gigem{'

for i in range(len(crib)):
    key += alpha_num[alpha_num.index(ct[i]) - alpha_num.index(crib[i]) % alpha_len]
print(key)
```
this prints:
```
mk3jk0
```

Which is somewhat concerning since it doesn't repeat any characters, which implies that the length of the key is either exactly 6 or longer. The key is not necessary for decoding the rest of the ciphertext since it is encoded using previous parts of the ciphertext which are known, but knowing the key length is important for knowing how large that offset is.

Since we don't see any repeats in the key found from the crib attack, we'll just start guessing key lengths starting with 6 until something coherent shows up. Luckily that happens at `key_len = 8`, and the following code appended to the snippet above will print a flag (full code in `solve.py`):

```py
flag += crib
key_len = 8

for i in range(len(key), len(ct)):
    flag += alpha_num[alpha_num.index(ct[i]) - alpha_num.index(ct[i-key_len]) % alpha_len]
print(flag)
```

and that outputs:
```
gigem{19comment se va? i think i might actually have some flaws in this poorly implemented autokey cipher gigem{ch3ck_y0ur_cryp70}
```

and we have our flag!
```
gigem{ch3ck_y0ur_cryp70}
```

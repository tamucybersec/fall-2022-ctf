# affine

Here's a ciphertext, maybe the name of this challenge means something important.

```
xtxbl{jmmtwb_ftsibo_shxxboz}
```

## Solution
Based on the challenge name, the flag is encrypted with an [affine cipher](https://en.wikipedia.org/wiki/Affine_cipher). In particular, each alphabetic character `p` (excluding the curly braces) was transformed into the provided encrypted character `e` via the equation `ap + b = e (mod 26)` for some unknown `a` and `b` (the alphabetic characters are converted to and from the integers 0 through 26). Our goal is to recover the secret key `(a, b)`, which will allow us to recover the plaintext. Since we know the flag has to start with "gi", we can create a system of 2 modular equations and solve it for `a` and `b`. However, I didn't feel like doing math, so I just tossed it into https://www.dcode.fr/affine-cipher, which provides a tool for brute-forcing the key (and even prints the resulting plaintext).

Flag: `gigem{affine_cipher_poggers}`

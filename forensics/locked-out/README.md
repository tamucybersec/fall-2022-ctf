# Locked Out

Oh no, I got locked out of my zip of hamster avatars! What will I do?

## Hint
I heard john thought my hamster was useful

## Solution:
the hint refers to the password cracking tool called john the ripper.

zip2john to get hash
```
zip2john nibs.zip > hash.txt
```

then john to crack the password
```
john hash.txt
```

One it's found, run the same command but with the --show flag to see the password
```
$ john-the-ripper hash.txt --show
nibs.zip:test124::nibs.zip:Nibbles.png, Lil_Nibs.png, CyberHam.png, Draft.png:nibs.zip

1 password hash cracked, 0 left
```

So now we have the password `test124` which we can use to unzip the zip and get the flag

```
gigem{uh_i_f0rg0t_t0_z1p_th3_fl4g}
```

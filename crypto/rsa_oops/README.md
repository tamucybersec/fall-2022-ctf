# RSA oops
I've created my RSA public modulus to be 1024 bits so there's no way you can break it. I'm so confident in RSA that I'll even decrypt stuff for you (as long as it's not the flag hehehe)

## Dev Notes
No files are given. 
Set up the server with 
```
make docker
make run
```

by default the server runs on port 8000

To clean everything:
```
make clean
```

## Solution
Chosen ciphertext attack that takes advantage of the homomorphic properties of RSA
See solve script

Flag: `gigem{r54_h4s_b0und5}`

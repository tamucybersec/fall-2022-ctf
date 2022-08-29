# Encryption as a Service
My all new EaaS technology is going to revolutionize crypto. It currently only does encryption, decryption will be implemented after the next round of investment funding.

Note: To save some time, the flag is composed from the following charset which is provided for your convenience: `abcdefghijklmnopqrstuvwxyz{}_`

## Dev Notes
Given files are everything except `key.txt` and `flag.txt`

To set up server:
```
make docker
make run
```

by default runs the service on port 7000

To clean up everything:
```
make clean
```

## Solution
This is a variation of an oracle attack. Since we see that the server appends the flag to the user message then uses pkcs17 padding to pad to 16 bytes, we can brute force the flag byte by byte. Find the offset that will push a new byte to the last block and then brute force that byte. It helps that AES operates in ECB mode so each block is encrypted individually.

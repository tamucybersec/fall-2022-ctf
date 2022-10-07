# pwn warmup
an easy one for you to start with

## Dev notes
This is likely going to be one of the 100-point challenges that we will provide help/writeup for

provided files are `pwn_warmup.c` and the binary

run docker:
```
make docker
make run
```


## Solution
This challenge is a simple buffer overflow challenge. The goal of this challenge is to somehow get the integer in the `globals` struct to be a non-zero value. 

Inspecting the source code, we see that `globals` has a 10 byte array followed by an integer. It is important to note that the array is only 10 bytes. 
```
struct {
    char name[10];
    int good;
} globals;
``` 

In `main()`, the program has a `0x10` byte array which is hexadecimal for 16. The program will read in 16 bytes to fill the buffer, then cast the buffer to the `globals.name` array. The only problem here is that the `name` array is only 10 bytes, but we are copying over 16. Thus we are overflowing the 10 byte array with 16 bytes which in turn, writes into the `globals.good` variable. 

So, when a user inputs 16 bytes into the buffer the 16 bytes will overflow into the `globals.good` variable and make it non-zero, allowing the user to obtain a shell. 

From there, type `cat flag.txt` and see the flag:
`gigem{too_ez_no_brain_needed}`

Commands to get flag:
```
nc <server> <port>
aaaaaaaaaaaaaaaa
cat flag.txt
```

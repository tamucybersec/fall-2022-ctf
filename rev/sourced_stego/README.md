# Sourced Stego
Hey look at that, a steg challenge that doesn't require any guessing, what a novel concept.
Given files are everything in the folder.

## Solution
Looks like hide.py takes in the flag, converts it to binary, then hides it in the last bit of of each blue pixel in the 'real_flag.png' file. We can extract the hidden message in a few ways. The easiest would be to throw the file into CyberChef and have it extract the bits for us. Another way is to write a script that also does it. 

Included here are both a script solution and a screenshot from CyberChef.

`gigem{real_flag_pls_submit_this}`

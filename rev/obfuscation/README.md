# obfuscated
No more interpreted languages or funny esolangs, time for some real reverse engineering and some real obfuscation

Only the `obfuscated` binary is given. Compile it with `make all`

## Solution
Opening this up in Ghidra doesn't provide a ton of help. The function that is called is obfuscated so ghidra doesn't recognize it. Using GDB to de-obfuscate the code and view the disassembly of it we can see that a string is placed on the stack and used as a comparison. 

The binary takes in a string from the user and compares it to the string on the stack after performing some operations on the user string. The disassembly makes it seem like all it does is XOR the index of each character with the character and compare that to the stored string. Just run the same operation on the string in the stack to recover the flag! Attached is a python script that does just that and gets the flag:

`gigem{this_program_probably_bypasses_most_antivirus}`

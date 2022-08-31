# empty
This program doesn't seem to do anything...


## Dev Notes
The only provided file is the binary `empty`


## Solution
Opening up the file in Ghidra, the decompiler doesn't do too much here, so it's time to stare at assembly.
It looks like the program will exit if there aren't 2 arguments when the program is run. There's also a strcmp instruction that will print "correct" if the argument matches a string in memory. Run the file with an argument in gdb. Break at the strcmp instruction (\*main+198), run it, and pull the string from the register.

Flag: `gigem{funny_inline_asm_confusion}`

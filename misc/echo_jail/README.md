# echo jail
Yet another echo, but not pwn this time! Try to escape from this jail, I'm pretty sure I filtered out everything sus

## Solution

Not all command substitution characters are filtered out. The backtick charater can be used to bypass the filter and get code execution. This can be used to trigger a reverse shell or just to print out the flag. 

Payload: ``` `cat /flag.txt` ```

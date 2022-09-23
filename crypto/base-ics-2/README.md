# BASE-ics 2
Maybe making the encoding less obvious might make things harder to break?
Idk I fell asleep in math class.

```
Z2lnZW17RW5Db0RpTmdfQ2hBbkdlU19SZVByRXNFblRhVGlPbl9Ob1RfZEF0QV8weEZPT0RTfQ==
```

## Solution

This is base64 encoding (the trailing equal signs are the giveaway). Again, use [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=WjJsblpXMTdSVzVEYjBScFRtZGZRMmhCYmtkbFUxOVNaVkJ5UlhORmJsUmhWR2xQYmw5T2IxUmZaRUYwUVY4d2VFWlBUMFJUZlE9PQo).

Flag: `gigem{EnCoDiNg_ChAnGeS_RePrEsEnTaTiOn_NoT_dAtA_0xFOODS}`

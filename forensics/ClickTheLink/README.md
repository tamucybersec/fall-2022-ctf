# ClickTheLink

Just do it... you know you want to ;)

## Solution
Since .docx files are really just .zip files in disguise, `unzip flag_kinda.docx` will spit out a bunch of files. Simply `grep -r gigem`:
```
docProps/app.xml:<!--Flag: gigem{docx_is_just_zip_poggers}-->
```

Flag: `gigem{docx_is_just_zip_poggers}`

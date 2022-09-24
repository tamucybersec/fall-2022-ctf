# Repair Shop

## Description

This image of my favorite meme got corrupted. Can you please repair it for me so I can cope with my CSCE 221 grades?

Tip: https://en.wikipedia.org/wiki/Portable_Network_Graphics#Examples

## Solution
Trying to open challenge.png gives an error about `IHDR: CRC error`

You could check manually or there's this tool called pngcheck that is pretty useful for finding where in the file the error is

```
$ pngcheck challenge.png 
challenge.png  CRC error in chunk IHDR (computed 920d5fe5, expected 69696969)
```

So there's a section with bytes 69696969 that's supposed to be 920d5fe5 presumably. We can get a hex dump of the image by running the following:
```
xxd challenge.png > chall.hex
```

Open up `chall.hex` and look for the bytes 69696969 and change it to the correct value. Then run the following to turn it back into an image:
```
xxd -r chall.hex > fixed.png
```

Open the image to get the flag:

```
gigem{s0lv1ng_ch4ll3ng3s}
```

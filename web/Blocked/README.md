# Blocked

## Description

Good luck getting access to my admin page. I blocked all IPs except for localhost.

## Dev notes

Start: `make run`
Stop: `make stop`

## Solution
A google search for "web ctf pretend to be localhost" finds mentions of an X-Forwarded-For header, which can be set by an attacker to spoof their IP address.
Opening up dev tools, adding that header and setting the value to 127.0.0.1 gets the flag

`gigem{n0t_th3_m0st_s3cur3_auth_m34sure}`

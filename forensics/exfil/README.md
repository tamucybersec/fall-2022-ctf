# exfil
(pretend there's some interesting and well thought out story here, then go look for the flag in the pcap)


## Solution

The pcap file contains a variety of dns requests for sites following the scheme `[character].google.com`. Following UDP stream 1 reveals that each request contains one charater from the flag.


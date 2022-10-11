# over the fence
Somebody dropped a note over my fence and I can't quite figure out what it means. You think you can help?
`Adenst agm3cr_ttwi{f33r}aangr__h_lc ! 4lcpc0k!110`


## Solution
As the name implies, the message is encrypted using a rail fence cipher. I plugged it into [CyberChef](https://gchq.github.io/CyberChef/#recipe=Rail_Fence_Cipher_Decode(6,10)&input=QWRlbnN0IGFnbTNjcl90dHdpe2YzM3J9YWFuZ3JfX2hfbGMgISA0bGNwYzBrITExMA) and brute-forced key values until I saw `gigem` emerge.

Flag: `gigem{r41l_f3nc3_c1ph3rs_r_c00l}`


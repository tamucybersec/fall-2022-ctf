# downloads
After the recent incident, we were able to get a capture of all of the network traffic coming to and from the victim host. Based on our knowledge of the malware, it likely downloaded a second stage from their C2 server around this time. See what you can find. 

## Solution
Given the title of the challenge, it seems that we should look for any sort of file transfer between two hosts. If we filter the pcap using `ftp`, we can see that a file called `second_stage.zip` was transferred. 
Change the filter to `ftp-data` and we see the data from the file mentioned before. Let's extract the file and unzip it to get the flag!

`gigem{un3ncryp3d_traff1c_l0ve_t0_s33_1t}`

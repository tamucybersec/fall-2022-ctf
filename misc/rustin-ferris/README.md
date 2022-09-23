# Rustin Ferris 

## Description 

We think our friend, Rustin Ferris, accidentally put something on Github (leaking a flag) that they weren't supposed to! In panic, they tried to cover up their mistakes, but they weren't the best. We lost the username to their Github, but we still have a link to their Twitter (https://twitter.com/FerrisRustin), and we think we might be able to find this flag still!

## Solution:
Scrolling the Twitter gives nothing useful, but there's a tweet that says deleting everything, so I thought maybe it was stored on the Internet Archive.

Turns out it was! going [here](https://web.archive.org/web/20220917214434/https://twitter.com/FerrisRustin/) reveals a deleted tweet that links to a github account.

That account has one repo, clone it down. nothing interesting in the files, but running git log shows a commit with the message "oops don't print the flag"

git diff against the commit before that, search for gigem, and find the flag:

`gigem{7h3_0nly_b00k_1_n33d_15_7h3_ru57_b00k}`

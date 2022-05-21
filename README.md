# Fall 2022 CTF

## Contributing

Instructions for contributing a challenge:

1. clone down the repo (don't use HTTPS authentication, use SSH)

2. make a branch with your challenge name
3. make a directory inside the corresponding challenge category (e.g. if I'm doing a CSRF chall, put it in `web/<challenge-name>`)
4. make your challenge; you should have a `README.md` file with the challenge name and description (sample below):
```
# <Challenge Name>
This is my description for my challenge!
## Solution
<to be written by the reviewer>
```
5. commit the files
6. push to the remote
7. open a pull request to merge your branch into `main`
8. get your challenge reviewed by someone else; the reviewer should add another commit to the branch that finishes the `## Solution` section in the challenge's `README.md`
9. merge the PR

<!--
## Docker

If you are writing a challenge that involves user interaction with a server, you **must** use Docker. Why?
1. reproducible builds - no more "but it works on my machine :("
2. sandboxing - containers are relatively isolated from your filesystem, and escapes are hard
3. port allocation - allow multiple services that require the same port to coexist
https://docs.docker.com/engine/install/ubuntu/

### Definitions
-->

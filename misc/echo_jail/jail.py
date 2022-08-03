from os import system

bad = '|&;()<>'

print("Echo program, only echoes, no RCE to see here")

while True:
    cmd = input(">>> ")

    for c in bad:
        if c in cmd:
            print("bruh")
            exit()
    system(f'/bin/bash -c "echo {cmd}"')

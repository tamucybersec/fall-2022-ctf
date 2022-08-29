from pwn import *
from Crypto.Util.Padding import pad

BLOCK_SIZE = 16
DEBUG = False
key_space = "abcdefghijklmnopqrstuvwxyz{}_"
flag = ""
test = 'aaaa'
guess_one = True
r = remote('0.0.0.0', 7000)

def byte(conn, flag, sig):
    for i in key_space: 
        guess = pad((i + flag).encode('utf-8'), BLOCK_SIZE)
        conn.recvuntil(b'>')
        conn.sendline(guess)
        conn.recvline()
        resp = conn.recvline().decode()[:32]

        if DEBUG:
            print('\t', guess, ':', resp)
        
        if resp == sig:
            flag = i + flag
            log.success("found byte: " + flag[0])
            return flag

    log.error("ERROR NO FLAG FOUND!")
    exit(1)

def byte2(conn, flag, sig):
    for i in key_space:
        for j in key_space: 
            guess = pad((i + j + flag).encode('utf-8'), BLOCK_SIZE)
            conn.recvuntil(b'>')
            conn.sendline(guess)
            conn.recvline()
            resp = conn.recvline().decode()[:32]

            if DEBUG:
                print('\t', guess,  ':', resp)

            if resp == sig:
                flag = i + j + flag
                log.success("found byte: " + flag[0])
                return flag
    log.error("ERROR NO FLAG FOUND!")
    exit(1)

while 'gigem' not in flag:
    # send a small message to grab the signature of last unknown byte
    r.recvuntil(b'>')
    r.sendline(test.encode('utf-8'))
    r.recvline()
    sig = r.recvline().decode().rstrip()

    # grab the signature of the unknown byte
    if len(flag) < 15:
        sig = sig[-32:]
    else:
        sig = sig[-64:-32]

    if DEBUG:
        log.info("sending: 'a' * %02d, current signature: %s" % (len(test), sig))

    if guess_one:
        flag = byte(r, flag, sig)
    else:
        flag = byte2(r, flag, sig)
        guess_one = True

    test += 'a'
    
    if (len(test) - 3) % BLOCK_SIZE == 0x6:
        test += 'a'
        guess_one = False

log.success("FINAL FLAG: %s" % flag)
r.close()
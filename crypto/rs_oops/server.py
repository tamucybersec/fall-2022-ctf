from Crypto.Util import number

n_length = 512 
flag = int.from_bytes(open('flag.txt', 'rb').read().strip(), 'big')

# generate primes
p = number.getPrime(n_length)
q = number.getPrime(n_length)

n = p * q
phi = (p-1) * (q-1)
e = 65537
d = pow(e, -1, phi)

print('Public Modulus: %s' % hex(n))
print('Public Key: %s' % hex(e))

print("\nHere's the flag: %s" % hex(pow(flag, e, n)))

print("I can decrypt any message for ya (not the flag ofc), just enter the hex value below")
try:
	user_input = int(input('> '), 16)
except:
	print("uh oh, something went wrong there. try again")
	exit(0)

if pow(user_input, d, n) == flag:
	print("sorry, you're going to have to work a little harder than that")
	exit(0)

print("Here's your decrypted message: 0x%x" % pow(user_input, d, n))



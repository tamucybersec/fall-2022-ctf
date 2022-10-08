from Crypto.Util import number
import random
import time

random.seed(time.time())
flag = number.bytes_to_long(open('flag.txt', 'rb').read().strip())

def get_check_resp(m, ed, n):
	try:
		resp = int(input('> '))
	except:
		print("\noops, there was an error. make sure to enter your answer as an integer. reconnect to try again.")
		return 0

	if pow(m, ed, n) != resp:
		print("\nAww man, that's not the right answer. See ya!")
		return 0

	print("\nWoohoo! That's correct!\n")
	return 1

# generate primes
p = number.getPrime(512)
q = number.getPrime(512)

n = p * q
phi = (p-1) * (q-1)
e = 65537
d = pow(e, -1, phi)

msg1 = random.randrange(n)
ctxt1 = random.randrange(n)
msg2 = 'encrypt me!'


print("Welcome to the RSA warmup! Solve these quick challenges to get the flag, good luck!")
print("Before we begin, you might need these to solve the challenges:")
print("n = %d" % n)
print("e = %d" % e)
print("d = %d\n" % d)

# challenge 1
print("-" * 5, "Challenge 1", "-" * 5)
print("Encrypt this message and send me your ciphertext (in decimal)")
print("msg1 = %d" % msg1)

if get_check_resp(msg1, e, n) == 0: 
	exit()

# challenge 2
print("-" * 5, "Challenge 2", "-" * 5)
print("Decrypt this message and send me the plaintext (in decimal)")
print("ctxt1 = %d" % ctxt1)

if get_check_resp(ctxt1, d, n) == 0: 
	exit()

# challenge 3
print("-" * 5, "Challenge 3", "-" * 5)
print("Encrypt this message and send me your ciphertext (in decimal)")
print("msg = %s" % msg2)

if get_check_resp(number.bytes_to_long(msg2.encode()), e, n) == 0:
	exit()

# challenge 4
print("-" * 5, "Challenge 4", "-" * 5)
print("Decrypt this message to get the flag!")
print("ctxt = %d" % pow(flag, e, n))


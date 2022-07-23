from PIL import Image
import binascii

def bin_to_ascii(c):
	n = int(c, 2)
	return binascii.unhexlify('%x' % n).decode()


flag_image = Image.open('./real_flag.png')
pixels = flag_image.load()
width, height = flag_image.size

flag = ''
char = ''

for i in range(width * height):
	x = i % width
	y = i // width
	
	r, g, b = pixels[x, y]

	char += str(b & 1) 
	
	if len(char) == 8:
		flag += bin_to_ascii(char)
		char = ''
		
		if '}' in flag:
			print(flag)
			break
	

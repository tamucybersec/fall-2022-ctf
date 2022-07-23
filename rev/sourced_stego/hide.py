from PIL import Image
import numpy as np

orig = Image.open('./original.png')
pixels = orig.load()
width, height = orig.size


with open('flag.txt', 'rb') as f:
    flag = f.read()

flag_bin = ''.join([bin(c)[2:].zfill(8) for c in flag])

for i in range(len(flag_bin)):
    x = i % width
    y = i // width

    r, g, b = pixels[x, y]
    pixels[x, y] = (r, g, (b&0xfe) | int(flag_bin[i]))

orig.save('real_flag.png', format='png')

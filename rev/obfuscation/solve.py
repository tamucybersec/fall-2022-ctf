#!/usr/bin/env python3

xor_str = 'ghefi~roazU{~bi}q|McfztvzucD~dn~SRGP{HIT\\vKEXDXFBDAN'
final_str = ''

i = 0
for letter in xor_str:
	final_str += chr(ord(letter) ^ i)
	i += 1 

print(final_str)

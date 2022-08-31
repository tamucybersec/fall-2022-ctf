#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char** argv) {
	__asm__ (
"push 0x4011be\n"
"ret"
	);

	char flag[] = "\x0e\x00\x0e\x0c\x04\x12\x0f\x1c\x07\x07\x10\x36\x00\x07\x05\x00\x07\x0c\x36\x08\x1a\x04\x36\x0a\x06\x07\x0f\x1c\x1a\x00\x06\x07\x14";
	
	if (argc != 2) {
		exit(0);
	}
	for (size_t i = 0; i < 33; i++) {
		flag[i] = flag[i] ^ (char)0x69;
	}
	if(!strncmp(flag, argv[1], 33)) {
		puts("correct!");
	}
}

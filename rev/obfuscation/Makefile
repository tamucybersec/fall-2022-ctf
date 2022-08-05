all: obfuscated.c
	gcc obfuscated.c -z execstack -o obfuscated

loaded: loaded.asm
	nasm -f elf64 loaded.asm && ld loaded.o -o loaded

clean:
	rm obfuscated loaded.o loaded

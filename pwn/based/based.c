#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

enum DEBUG_MODE{False, True};

char* vuln() {
	char guess[8];
	puts("Password:");
	scanf("%16s", guess);

	if(strncmp(guess, "hunter2", 7) != 0) {
		puts("Password incorrect.");
		exit(-1);
	}
}

int main() {
	// Ignore, stuff to set up server I/O correctly
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	
	enum DEBUG_MODE debug = False;

	puts("Username:");
	char username[0x100];
	fgets(username, 0x100, stdin);

	vuln();

	if (debug) {
		puts("Entering debug mode");
		system("/bin/sh");
	} else {
		puts("Nothing here yet, come back later.");
	}
}

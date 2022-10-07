#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct {
    char name[10];
    int good;
} globals;

int main() {
    // Ignore, stuff to set up server I/O correctly
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

    char n[0x10];

    puts("what's your name?");
    fgets(n, 0x10, stdin);

    puts("storing name...");
    strcpy(globals.name, n);
    if(globals.good) {
        system("/bin/sh");
    } else {
        puts("not cool :(");
    }
}

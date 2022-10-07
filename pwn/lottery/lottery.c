#include <stdio.h>
#include <stdlib.h>

void print_flag() {
    char buf[128];
    FILE* f = fopen("flag.txt", "r");
    fgets(buf, sizeof(buf), f);
    puts(buf);
}

void vuln() {
    int seed = time(NULL);
    char name[8];
    puts("What's your name?");
    fgets(name, 16, stdin);

    // initialize the random number generator with a totally unknown seed
    srand(seed);
    int actual = rand();

    int guess = 0;
    puts("Guess a lucky number:");
    scanf("%d", &guess);

    if (actual == guess) {
        printf("Congrats, %s! Here's a flag:\n", name);
        print_flag();
    } else {
        printf("It was %d :pensive:, better luck next time!", actual);
    }
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
}

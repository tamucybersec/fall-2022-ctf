#include <stdio.h>
#include <stdlib.h>

int check(unsigned long n, unsigned long fav) {
        if ((n & 0xffff) == (fav & 0xffff)) {
                return 1;
        }
        return 0;
}

void vuln() {
        unsigned long fav;
        char resp;
        unsigned long a;
        unsigned long b;
        unsigned long c;
        unsigned long d;

        fav = rand();

        do {
                // ask user for input
                printf("Please enter a: ");
                scanf("%lu", &a);
                printf("Please enter b: ");
                scanf("%lu", &b);
                printf("Please enter c: ");
                scanf("%lu", &c);
                printf("Please enter d: ");
                scanf("%lu", &d);

                // perform some calculations on the numbers
                d = d + c;
                c = c ^ b;
                b = b - a;

                if (check(d, fav)) {
                        printf("Woohoo! You correctly guessed my favorite number!\n");
                        printf("Here's a little something for your hard work: %lx\n", &d);
                } else {
                        printf("I don't really like that number:(\n");
                }

                // go again?
                printf("Would you like to go again? (y/n) ");
                scanf("%s", &resp);

        } while (resp == 'Y' || resp == 'y');

        return;
}

void welcome() {
        printf("Welcome to this fun program!\n");
        printf("Try to guess my favorite number, I bet you can't!!\n");

}

int main() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
        welcome();
        vuln();

        printf("bye now\n");
	return 0;
}

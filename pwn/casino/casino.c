#include <stdio.h>
#include <stdlib.h>
#define STAR_COST 1u
#define FLAG_COST 13371337u
#define CHANCE 1337u

int balance = 10;

void gamble() {
    int bet = 0;
    puts("Enter your bet:");
    scanf("%d", &bet);
    if (bet > balance) {
        puts("You don't have enough money to bet that amount!");
        return;
    }
    balance -= bet;
    if (rand() % CHANCE == 0) {
        puts("You won!");
        balance += bet * 2;
    } else {
        puts("You lost, better luck next time!");
    }
}

void shop() {
    printf("Your current balance is $%d. What do you want to buy?\n", balance);
    puts("  1. hug");
    puts("  2. gold star");
    puts("  3. flag");

    int choice = -1;
    scanf("%d", &choice);
    switch (choice) {
        case 1:
            puts("Have a free hug!");
            break;
        case 2:
            if (balance >= STAR_COST) {
                balance -= STAR_COST;
                puts("Have a gold star!");
            } else {
                puts("You don't have enough money for a gold star!");
            }
            break;
        case 3:
            if (balance >= FLAG_COST) {
                balance -= FLAG_COST;
                puts("Have a flag!");
                char buf[128];
                FILE* f = fopen("flag.txt", "r");
                fgets(buf, sizeof(buf), f);
                puts(buf);
            } else {
                puts("You don't have enough money for a gold flag!");
            }
            break;
        default:
            puts("We don't have that here.");
            break;
    }
}

int main() {
    int choice = -1;
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    srand(time(NULL));
    puts("Welcome to my casino!");
    while (1) {
        puts("Pick one of the following options:");
        puts("  1. gamble");
        puts("  2. spend winnings");
        puts("  3. exit");
        puts("Enter your choice:");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                gamble();
                break;
            case 2:
                shop();
                break;
            case 3:
                puts("Bye!");
                exit(0);
                break;
            default:
                puts("Invalid choice, try again.");
                break;
        }
    }
}

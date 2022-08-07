#include <stdio.h>
#include <stdlib.h>

int main() {
    char flag[] = "ghefi~roazU{~bi}q|McfztvzucD~dn~SRGP{HIT\\vKEXDXFBDAN";
//    char flag[] = "gigem{this_program_probably_bypasses_most_antivirus}";

    char buf[53];
    __asm__ (
"   mov %0, %%rsi\n\t"
"   mov $0, %%rax\n\t"
"   mov $0, %%rdi\n\t"
"   mov $53, %%rdx\n\t"
"   syscall\n\t"
    :
    :"r" (buf)
    );

    for (int i = 0; i < 52; i++) { 
        if ((char)(buf[i]^i) != flag[i]) {
            puts("almost there!");
            exit(-1);
        }
    }
    puts("good job!");
    
}

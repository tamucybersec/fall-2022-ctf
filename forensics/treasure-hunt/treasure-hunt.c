#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

#define MAX_BUF_SIZE 64

void encrypt(char* flag, int len) {
    for (int i = 0; i < len; ++i) {
        flag[i] ^= 0x42;
    }
}

void zero(char* flag, int len) {
    for (int i = 0; i < len; ++i) {
        flag[i] = 0;
    }
}

void copy(char* dst, char* src, int len) {
    for (int i = 0; i < len; ++i) {
        dst[i] = src[i];
    }
}

void core_dump() {
    // kaboom! the program will die here
    abort();
}

void treasure_chest(char* flag, int len) {
    char flag_backup[MAX_BUF_SIZE] = {0};
    copy(flag_backup, flag, len);
    encrypt(flag_backup, len);
    zero(flag, len);
    core_dump();
}

int main() {
    char* flag = calloc(MAX_BUF_SIZE, 1);
    int fd = open("flag.txt", O_RDONLY);
    int len = read(fd, flag, MAX_BUF_SIZE);
    treasure_chest(flag, len);
}

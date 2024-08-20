#include<stdio.h>
#include<string.h>

int main() {
    char str1[12];
    gets(str1);
    int length = 0;
    int test = 0, special = 0;

    for (int i = 0; str1[i] != '\0'; i++) {
        length++;
    }
    if (length < 6) {
        printf("invalid");
        return 0;
    }


    for (int j = 0; str1[j] != '\0'; j++) {
        if ((str1[j] >= 97 && str1[j] <= 122) || (str1[j] >= 65 && str1[j] <= 90)) {
            test++;
        } else if (str1[j] == 35 || str1[j] == 36 || str1[j] == 64) {
            special++;
        } else {
            printf("invalid");
            return 0;
        }
    }

    if (special > 0 && test > 0) {
        printf("valid");
    } else {
        printf("invalid");
    }

    return 0;
}

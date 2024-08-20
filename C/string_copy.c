#include<stdio.h>
#include<ctype.h>
#include<string.h>
int main(){
    char str1[100],str2[100];
    gets(str1);
    strcpy(str2,str1);
    printf("%s",str2);
}

#include<stdio.h>
#include<string.h>
int main(){
    char s1[100]="Good";
    char s2[100]="bad";
    char s3[100]="very";
    strcat(s1,strcat(s2,strcat(s3,(strcat("hai","hello")))));

}

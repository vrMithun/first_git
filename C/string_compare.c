#include<stdio.h>
#include<ctype.h>
#include<string.h>
int main(){
    char str1[100],str2[100];
    gets(str1);
    gets(str2);
    int k=strcmp(str1,str2);
    if(k==0){
        return 1;
    }
    else{
        return 0;
    }
}

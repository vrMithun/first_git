#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main(){
    char str[100];
    gets(str);
    for(int i=0;i<strlen(str);i++){
        int count=0;
        for(int j=0;j<strlen(str);j++){
            if(str[i]==str[j]){
                count++;
            }
        }

    }
}

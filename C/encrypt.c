#include<stdio.h>
int main(){
    char str[10];
    gets(str);
    for(int i=0;i<10;i++){
        if(str[i]=='z'){
            str[i]='b';
        }
        else if(str[i]=='y'){
            str[i]='a';
        }
        else{
            str[i]+=2;
        }
    }
    puts(str);
}

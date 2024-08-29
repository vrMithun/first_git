#include<stdio.h>
#include<ctype.h>
#include<string.h>
int main(){
    int test=1;
    char str[10];
    gets(str);
    int length=0,count=0;
    for(int i=0;str[i]!='\0';i++){
        length=length+1;
    }
    for(int j=0;str[j]!='\0';j++){
        if (str[j]>=65 && str[j]<=90){
            count=str[j]-65+1;
        }
        if (str[j]>=97 && str[j]<=122){
            count=str[j]-97+1;
        }
        if(test%2!=0){
            for(int k=0;k<count;k++){
                printf("%c",'@');

            }
        }
        else{
            for(int k=0;k<count;k++){
                printf("%c",'!');

            }
        }
        test++;
    }
}

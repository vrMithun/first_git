#include<stdio.h>
int main(){
    char color[]="blue";
    int length=sizeof(color)/sizeof(color[0]);
    for(int i=0;i<length-1;i++){
        printf("%c",color[i]);
    }
    printf("\n%d",sizeof(color));
}

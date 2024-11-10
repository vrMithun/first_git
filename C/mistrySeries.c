#include<stdio.h>
int main(){
    int a=5;
    int temp=a;
    printf("%d ",a);
    for(int i=0;i<=13;i++){
        temp-=1;
        printf("%d ",temp);
        temp-=2;
        printf("%d ",temp);
        temp+=5;
        printf("%d ",temp);
        temp+=4;
        printf("%d ",temp);
    }

}

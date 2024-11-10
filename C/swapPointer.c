#include<stdio.h>
int main(){
    int a=10;
    int b=20;
    int *t=&a;
    printf("%p,%p\n",&a,&b);
    swap(a,b);
    printf("%p,%p",&a,&b);
}
void swap(int *p,int *q){
    int *t=p;
    *p=*q;
    *q=*t;
    return
}

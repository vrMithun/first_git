#include<stdio.h>
int main(){
    int k=1;
    int l=2;
    printf("%d",*&k+*&l);
}

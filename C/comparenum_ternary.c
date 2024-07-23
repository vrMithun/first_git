#include<stdio.h>
int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    (a>b)?(a>c)?printf("a is greatest"):(a==c)?printf("a and c"):printf("c is greatest"):(b>c)?printf("b is greatest"):(b<c)?printf("c is greatest"):(a==b)?printf("a,b,c"):printf("a and c");n
    return 0;
}

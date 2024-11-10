#include<stdio.h>
#include<stdlib.h>
int main(){
    int *ptr;
    ptr=calloc(4,sizeof(*ptr));
    ptr[0]=2;
    ptr[1]=4;
    ptr[2]=6;
    ptr[3]=4;
    printf("%d",*ptr);
    free(ptr);
    ptr=NULL;
    printf("%d",*ptr);
}

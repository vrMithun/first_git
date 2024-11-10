#include<stdio.h>
int main(){
    /*int arr[]={1,2,3,4,5};
    int length=sizeof(arr)/sizeof(arr[0]);
    printf("%p",&arr);
    for(int i=0;i<length;i++){
        printf("%p\n",&arr[i]);
    }
    */
    int k=10;
    int *p=&k;
    int **q=&p;
    printf("%p,%p\n",q,&p);
    printf("%p,%p\n",*q,&k);
    printf("%d,%d\n",**q,k);
}

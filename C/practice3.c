#include<stdio.h>
#include<stdlib.h>
int* arr(int arr[],int length){
    int *ptr=calloc(2*length,sizeof(int));
    for(int i=0;i<length;i++){
        ptr[i]=arr[i];
    }
    return ptr;
}
int main(){
    int array[10]={1,2,3,4,5,6,7,8,9,10};
    int* result=arr(array,10);
    for(int i=0;i<20;i++){
        printf("%d ",result[i]);
    }
}

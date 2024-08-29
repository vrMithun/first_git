#include<stdio.h>
int sum(int arr[],int n,int length){

    if (n==length){
            return 0;
    }
    else{
        return arr[n]+sum(arr,n+1,length);
    }
}
int main(){
    int arr[]={1,2,3,4};
    int length=sizeof(arr)/sizeof(arr[0]);
    printf("%d",sum(arr,0,length));
}

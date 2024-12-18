#include<stdio.h>
#include<stdlib.h>
int main(){
    int arr[]={1,2,2,3,2,2,4,4,4,4,4};
    int length=sizeof(arr)/sizeof(arr[0]);
    printf("%d",freq(arr,length));
}
int freq(int arr[],int length){
    sort(arr,length);
    int max=0;
    int count=1;
    int result;
    int i;
    for( i=0;i<length-1;i++){
        if(arr[i]==arr[i+1]){
            count++;
        }
        else if(arr[i]!=arr[i+1] && max<count){
            max=count;
            result=arr[i];
            count=1;
        }
    }
    if(max<count){
        result=arr[i];
    }
    return result;
}
void sort(int arr[],int length){
    for(int i=0;i<length;i++){
        for(int j=0;j<length-1;j++){
            if (arr[j]>arr[j+1]){
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
}

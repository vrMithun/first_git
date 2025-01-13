#include <iostream>
using namespace std;

void Sort(int arr[],int length){
    for(int i=length-1;i>=0;i--){
        for(int j=0;j<i;j++){
            if(arr[j]>arr[j+1]){
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
}

int main(){
    int arr[]={7,12,9,15,19,32,56,70};
    int length=sizeof(arr)/sizeof(arr[0]);
    Sort(arr,length);
    for(int i=0;i<length-2;i++){
        printf("%d ",arr[i]);
    }
}

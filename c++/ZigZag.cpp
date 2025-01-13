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
    int arr[]={4,3,7,8,6,2,1};
    int length=sizeof(arr)/sizeof(arr[0]);
    Sort(arr,length);
    int i=0;
    while(i<length/2){
        printf("%d ",arr[i]);
        printf("%d ",arr[length-1-i]);
        i++;
    }
    if(length%2!=0){
        printf("%d ",arr[length/2]);
    }

}

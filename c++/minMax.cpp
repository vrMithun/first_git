#include <iostream>
using namespace std;

int main(){
    int arr[]={0,1,3,4,5,6,7,8,10};
    int length=sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<length/2;i++){
        printf("%d ",arr[length-1-i]);
        printf("%d ",arr[i]);
    }
    if(length%2!=0){
        printf("%d ",arr[length/2]);
    }
}

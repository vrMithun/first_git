#include<iostream>
#include<vector>
using namespace std;

void BubbleSort(vector<int>& arr,int length){//use & for call by reference. instead of using * it is more simpler. we can directly
    int temp;                                   //access the vector instead of using the pointer
    for(int i=length-1;i>0;i--){                // we are saying to the compiler that we are calling the vector by reference
        for(int j=0;j<i;j++){                   //c language doenst have this feature we use pointer for it
            if(arr[j]>arr[j+1]){
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
}

int main(){
    vector<int> arr={9,8,7,6,5};
    int length=arr.size();
    BubbleSort(arr,length);
    for(int i=0;i<length;i++){
        cout<<arr.at(i)<<" ";
    }
}

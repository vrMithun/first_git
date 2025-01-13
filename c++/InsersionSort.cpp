#include<iostream>
#include<vector>
using namespace std;

void InsersionSort(vector<int>& arr,int length){
    int key;
    int j;
    for(int i=1;i<length;i++){
        key=arr.at(i);
        j=i-1;
        while (j>=0 && arr[j]>key){
            arr.at(j+1)=arr.at(j);
            j--;
        }
        arr.at(j+1)=key;
    }
}

int main(){
    vector<int> myvect={3,2,7,5,9,3};
    int length=myvect.size();
    InsersionSort(myvect,length);
    for(int i=0;i<length;i++){
        cout<<myvect.at(i)<<" ";
    }
}

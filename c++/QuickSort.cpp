#include<iostream>
#include<vector>
using namespace std;
int Partition(vector<int>& arr,int low,int high);

void QuickSort(vector<int>& arr,int low,int high){
    if (low<high){
        int pivotIndex=Partition(arr,low,high);
        QuickSort(arr,low,pivotIndex-1);
        QuickSort(arr,pivotIndex+1,high);
    }
}

int Partition(vector<int>& arr,int low,int high){
    int pivot=arr[low];
    int i=low+1;
    for(int j=low+1;j<=high;j++){
        if (arr[j]<pivot){
            swap(arr[i],arr[j]);
            i++;
        }
    }
    swap(arr[low],arr[i-1]);
    return i-1;
}

int main(){
    vector<int> arr={9,8,7,1,2,3};
    QuickSort(arr,0,arr.size()-1);
    for(int i=0;i<arr.size();i++){
        cout<<arr[i]<<" ";
    }

}

#include <iostream>
#include<vector>
using namespace std;
int Partition(vector<int>& vect,int low,int high);
void InsersionSort(vector<int>& vect){
    int length=vect.size();
    for(int i=1;i<length;i++){
        int key=vect[i];
        int j=i-1;
        while(j>=0 && vect[j]>key){
            vect[j+1]=vect[j];
            j--;
        }
        vect[j+1]=key;
        for(int i=0;i<vect.size();i++){
            cout<<vect[i]<<" ";
        }
        cout<<"\n";
    }
}



void BubbleSort(vector<int>& vect){
    int length=vect.size();
    for(int i=length-1;i>0;i--){
        for(int j=0;j<i;j++){
            if(vect[j]>vect[j+1]){
                swap(vect[j],vect[j+1]);
            }
        }
        for(int i=0;i<vect.size();i++){
            cout<<vect[i]<<" ";
        }
        cout<<"\n";
    }
}

void BubbleSortFlag(vector<int>& vect){
    int length=vect.size();
    for(int i=length-1;i>0;i--){
        bool flag=false;
        for(int j=0;j<i;j++){
            if(vect[j]>vect[j+1]){
                swap(vect[j],vect[j+1]);
                flag=true;
            }
        }
        for(int i=0;i<vect.size();i++){
            cout<<vect[i]<<" ";
        }
        cout<<"\n";
        if(!flag){
            break;
        }
    }
}

void SelectionSort(vector<int>& vect){
    for(int i=0;i<vect.size();i++){
        int mini=i;
        for(int j=i+1;j<vect.size();j++){
            if(vect[mini]>vect[j]){
                mini=j;
            }
        }
        if(mini!=i){
            swap(vect[mini],vect[i]);
        }
        for(int i=0;i<vect.size();i++){
            cout<<vect[i]<<" ";
        }
        cout<<"\n";
    }

}

void QuickSort(vector<int>& vect,int low,int high){
    if (low<high){

        int index=Partition(vect,low,high);
        QuickSort(vect,low,index-1);
        QuickSort(vect,index+1,high);
    }
}

int Partition(vector<int>& vect,int low,int high){
    int pivot=vect[high];
    int p=low;
    for(int i=low;i<high;i++){
        if(vect[i]<pivot){
            swap(vect[i],vect[p]);
            p++;
        }
    }
    swap(vect[p],vect[high]);
    return p;
}

int RadixSort(vector<int>& vect){
    int length=vect.size();
    int maxi=*max_element(vect.begin(),vect.end());
    int exp=1;
    while(maxi/exp>0){
        vector<vector<int>> bucket[10];
        for(int val:vect){
            int index=(val/exp)%10;
            bucket[index].push_back(val);
        }
    }
    for(auto& myvect:bucket){
        for(int val:myvect){

        }
    }
}

int main(){
    vector<int> vect={1,2,3,4,9,6,5};
    QuickSort(vect,0,vect.size()-1);
    for(int i=0;i<vect.size();i++){
            cout<<vect[i]<<" ";
    }
    cout<<"\n";
}

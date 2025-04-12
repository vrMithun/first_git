#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

void DisplayVector(vector<int>& vect);

void SelectionSort(vector<int>& vect){
    int length=vect.size();
    int totalIter=length/2;
    for(int i=0;i<totalIter;i++){
        int left=i;
        int right=length-i-1;
        int minimum=left;
        int maximum=left;
        for(int j=left;j<=right;j++){
            if(vect.at(j)>vect.at(maximum)){
                maximum=j;
            }
            else if(vect.at(j)<vect.at(minimum)){
                minimum=j;
            }
        }
        cout<<"left="<<left<<"right"<<right<<"\n";
        cout<<"minimum="<<vect.at(minimum)<<" maximum="<<vect.at(maximum)<<"\n";
        swap(vect.at(left),vect.at(minimum));
        if(maximum==left){
            maximum=minimum;
        }
        swap(vect.at(right),vect.at(maximum));
        DisplayVector(vect);
        cout<<"\n";
    }
}



void InsersionSort(vector<float>& vect){
    for(float i=1;i<vect.size();i++){
        int key=vect.at(i);
        int j=i-1;
        while(j>=0 && vect.at(j)>key){
            vect.at(j+1)=vect.at(j);
            j--;
        }
        vect.at(j+1)=key;
    }
}

void BubbleSort(vector<int>& vect){
    int length=vect.size();
    for(int i=length-1;i>0;i--){
        bool flag=false;
        for(int j=0;j<i;j++){
            if(vect[j]>vect[j+1]){
                swap(vect[j],vect[j+1]);
                flag=true;
            }
        }
        if(!flag){
            break;
        }
    }
    DisplayVector(vect);
}

void DisplayVector(vector<int>& vect){
    for(int i=0;i<vect.size();i++){
        cout<<vect.at(i)<<" ";
    }
}

int Partition(vector<int>& myvect,int left,int right){
    int pivot=right;
    int pointer=left-1;
    for(int i=left;i<right;i++){
        if(myvect.at(i)<myvect.at(pivot)){
            pointer++;
            swap(myvect.at(pointer),myvect.at(i));
        }
    }
    swap(myvect.at(pointer+1),myvect.at(pivot));
    return pointer+1;
}

void QuickSort(vector<int>& myvect,int left,int right){
    if(left<right){
        int Index=Partition(myvect,left,right);
        QuickSort(myvect,left,Index-1);
        QuickSort(myvect,Index+1,right);
    }
}

void Merge(vector<int>& myvect,int left1,int right1,int left2,int right2){
    vector<int> testvect;
    int i=left1;
    int j=left2;
    while(i<=right1 && j<=right2){
        if(myvect.at(i)>myvect.at(j)){
            testvect.push_back(myvect.at(j));
            j++;
        }
        else{
            testvect.push_back(myvect.at(i));
            i++;
        }
    }
    while(i<=right1){
        testvect.push_back(myvect.at(i));
        i++;
    }
    while(j<=right2){
        testvect.push_back(myvect.at(j));
        j++;
    }
    for(int i=left1;i<=right2;i++){
        myvect.at(i)=testvect.at(i-left1);
    }
}

void MergeSort(vector<int>& myvect,int left,int right){
    int mid=(left+right)/2;
    if(left==right){
        return;
    }
    MergeSort(myvect,left,mid);
    MergeSort(myvect,mid+1,right);
    Merge(myvect,left,mid,mid+1,right);
}

void BucketSort(vector<float>& myvect){
    int length=myvect.size();
    if(length==1){
        return;
    }
    float minval=myvect.at(0),maxval=myvect.at(0);
    for(int i=1;i<length;i++){
        if(minval>myvect.at(i)){
            minval=myvect.at(i);
        }

        else if (maxval < myvect.at(i)) {
            maxval=myvect.at(i);
        }
    }
    float range=maxval-minval;
    int totalbucket=floor(sqrt(length));
    vector<vector<float>> buckets(totalbucket);
    for(int i=0;i<length;i++){
        int index=floor((myvect.at(i)-minval)*totalbucket/range);
        if (index == totalbucket) {
            index--;
        }
        buckets.at(index).push_back(myvect.at(i));
    }
    for(auto& bucket:buckets){
        InsersionSort(bucket);
    }
    int i=0;
    for(auto& bucket:buckets){
        for(auto& val:bucket){
            myvect.at(i)=val;
            cout<<val<<" ";
            i++;
        }
    }
}

void heapify(vector<int>& myvect,int length,int StartIndex){
    int greatest=StartIndex;
    int left=StartIndex*2+1;
    int right=StartIndex*2+2;
    if(left<length && myvect.at(StartIndex)<myvect.at(left)){
        greatest=left;
    }
    if(right<length && myvect.at(StartIndex)<myvect.at(right)){
        greatest=right;
    }
    if(greatest!=StartIndex){
        swap(myvect.at(greatest),myvect.at(StartIndex));
        heapify(myvect,length,greatest);
    }
}

void HeapSort(vector<int>& myvect){
    int length=myvect.size();
    for(int i=length/2-1;i>=0;i--){
        heapify(myvect,length,i);
    }
    for(int i=length-1;i>=0;i--){
        swap(myvect.at(0),myvect.at(i));
        heapify(myvect,i,0);
    }
}

int main(){
    vector<int> myvect={214,32,122,111};
    HeapSort(myvect);
    DisplayVector(myvect);

}

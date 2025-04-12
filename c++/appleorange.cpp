#include<iostream>
#include<vector>
using namespace std;

vector<int> ApplesAndOranges(int s,int t,int a,int b,vector<int>& apples,vector<int>& oranges){
    vector<int> mycount;
    int temp=0;
    for(int i=0;i<apples.size();i++){
        apples.at(i)+=a;
        if(apples.at(i)>=s && apples.at(i)<=t){
            temp++;
        }
    }
    mycount.push_back(temp);
    temp=0;
    for(int i=0;i<oranges.size();i++){
        oranges.at(i)+=a;
        if(oranges.at(i)>=s && oranges.at(i)<=t){
            temp++;
        }
    }
    mycount.push_back(temp);
    return mycount;
}

int main(){
    int s=7;
    int t=10;
    int a=4;
    int b=12;
    vector<int> apples={2,3,-4};
    vector<int> oranges={3,-2,-4};
    vector<int> myvect=ApplesAndOranges(s,t,a,b,apples,oranges);
    cout<<myvect.at(0)<<"\n";
    cout<<myvect.at(1);
}

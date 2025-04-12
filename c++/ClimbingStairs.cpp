#include<iostream>
#include<vector>
using namespace std;

int stairs(int n,vector<int>& memo){
    if(n==1 || n==0){
        return 1;
    }
    if(n<0) return 0;
    if(memo.at(n)!=-1) return memo.at(n);
    return memo.at(n)=stairs(n-1,memo)+stairs(n-2,memo);
}

int main(){
    int n;
    cin>>n;
    vector<int> memo(n+1,-1);
    cout<<stairs(n,memo);
}

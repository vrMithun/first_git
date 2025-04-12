#include<iostream>
#include<vector>
using namespace std;

vector<int> memo;

int fibo(int n,vector<int>& memo){
    if(n==0) return 0;
    if(n==1) return 1;
    if(memo.at(n)!=-1) return memo.at(n);
    return memo.at(n)=(fibo(n-1,memo)+fibo(n-2,memo));
}

int main(){
    int n;
    cin>>n;
    memo.resize(n+1,-1);
    cout<<fibo(n,memo);
}

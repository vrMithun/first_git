#include<iostream>
#include<vector>
using namespace std;

int fibo(int n,vector<int>& dp){
    if(dp.at(0)==-1){
        dp.at(0)=0;
    }
    if(dp.at(1)==-1){
        dp.at(1)=1;
    }
    for(int i=2;i<=n;i++){
        dp.at(i)=dp.at(i-1)+dp.at(i-2);
    }
    return dp.at(n);
}

int main(){
    int n;
    cin>>n;
    vector<int> dp(n+1,-1);
    cout<<fibo(n,dp);
}

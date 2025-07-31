#include<iostream>
#include<vector>
#include <bits/stdc++.h>
using namespace std;

int minimumCost(vector<int>& cost) {
    sort(cost.begin(),cost.end());
    int result=0;
    int i=cost.size()-1;
    int bought=0;
    while(i>=0){
        if(bought<2){
            result+=cost[i];
            bought++;
        }
        else{
            bought=0;
        }
        i--;
    }
    return result;
}

int main(){
    vector<int> myvect= {6,5,7,9,2,2};
    cout<<minimumCost(myvect);
}

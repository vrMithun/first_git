#include<iostream>
#include<vector>
using namespace std;

bool xorGame(vector<int>& nums) {
    int myxor=0;
    for(int i:nums){
        myxor=myxor^i;
    }
    if(myxor==0){
        return true;
    }
    else if(nums.size()%2==0){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    int a=0^3;
    cout<<a;
}

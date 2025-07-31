#include<iostream>
#include<vector>
#include<bits/stdc++.h>
#include<string.h>
using namespace std;

int minimumSum(int num){
    string mystr=to_string(num);
    sort(mystr.begin(),mystr.end());
    int left=0;
    int right=mystr.size()-1;
    int result=0;
    while(left<right){
        int num1=(mystr[left]-'0')*10;
        int num2=(mystr[right]-'0');
        result=result+num1+num2;
        left++;
        right--;
    }
    return result;
}


int main(){
    int myint=2932;
    cout<<minimumSum(myint);
}

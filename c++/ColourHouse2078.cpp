#include<iostream>
#include<vector>
using namespace std;

int maxDistance(vector<int>& colors) {
    int left=0;
    int right=colors.size()-1;
    int result=0;
    while(left<right){
        if(colors[left]!=colors[right]){
            result=max(result,right-left);
        }
        left++;
    }
    left=0;
    right=colors.size()-1;
    int result2=0;
    while(left<right){
        if(colors[left]!=colors[right]){
            result2=max(result2,right-left);
        }
        right--;
    }
    return max(result,result2);
}

int main(){
    vector<int> colors={1,1,1,1,1,1,1};
    cout<<maxDistance(colors);
}

#include<iostream>
#include<vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    int left=0;
    int right=nums.size()-1;
    vector<int> result;
    while(left<right){
        int mysum=nums.at(left)+nums.at(right);
        if(mysum==target){
            result.push_back(left);
            result.push_back(right);
        }
        else if(mysum>target){
            if(nums.at(left)>nums.at(right)){
                left++;
            }
            else{
                right--;
            }
        }
        else{
            if(nums.at(left)>nums.at(right)){
                right--;
            }
            else{
                left++;
            }
        }
    }
    return result;
}

int main(){
    vector<int> myvect={2,7,6,5};
    vector<int> vect=twoSum(myvect,9);
    for(int i=0;i<vect.size();i++){
        cout<<vect.at(i)<<" ";
    }
}

#include<iostream>
#include<vector>
using namespace std;


int trap(vector<int>& height) {
    int right=height.size()-1;
    int left=0;
    int rightmax=0;
    int leftmax=0;
    int result=0;
    while(left<right){
        if(height.at(left)<height.at(right)){
            if(leftmax<height.at(left)){
                leftmax=height.at(left);
            }
            else{
                result+=leftmax-height.at(left);
            }
            left++;
        }
        else{
            if(rightmax<height.at(right)){
                rightmax=height.at(right);
            }
            else{
                result+=rightmax-height.at(right);
            }
            right--;
        }
    }
    return result;

}

int main(){
    vector<int> myvect={4,2,0,3,2,5};
    cout<<trap(myvect);
}

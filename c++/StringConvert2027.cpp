#include<iostream>
#include<vector>
using namespace std;

int minimumMoves(string s) {
    int i=0;
    int result=0;
    while(i<s.size()){
        if(s[i]=='X'){
            result++;
            i+=3;
        }
        else{
            i++;
        }
    }
    return result;
}

int main(){
    string mystr="OXOX";
    cout<<minimumMoves(mystr);
}

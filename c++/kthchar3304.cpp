#include<iostream>
#include<vector>
using namespace std;

string mystr="a";

string helper(string& str){
    int length=str.length();
    for(int i=0;i<length;i++){
        str=str+char(str.at(i)+1);
    }
    return str;
}

char kthCharacter(int k) {
    while(mystr.length()<k){
        helper(mystr);
    }
    return mystr.at(k-1);
}

int main(){
    cout<<kthCharacter(5);
}

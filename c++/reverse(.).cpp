#include<iostream>
#include<vector>
#include<ctype.h>
using namespace std;

void reverseString(string& mystring){
    int length=mystring.length();
    string test="";
    int i=0;
    vector<string> myvect;
    while(i<length-1){
        if(isalpha(mystring[i])){
            test=test+mystring[i];
        }
        /*else if(mystring[i]=="." && mystring[i+1]=="."){
            myvect.push_back(test);
            test="";
            i=i+2;
        }*/
        else{
            myvect.push_back(test);
            test="";
        }
        i++
    }
    for(int i=myvect.size();i>=0;i--){
        if(i==0){
            cout<<myvect.at(i);
            continue;
        }
        cout<<myvect.at(i)<<".";
    }
}

int main(){
    string mystring;
    cin>>mystring;
    reverseString(mystring);
}

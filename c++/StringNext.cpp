#include<iostream>
#include<vector>
using namespace std;

void shift(string& mystring){
    for(int i=0;i<mystring.length();i++){
        mystring[i]=mystring[i]+1;
    }
}

int main(){
    string mystring;
    cin>>mystring;
    shift(mystring);
    cout<<mystring;
}

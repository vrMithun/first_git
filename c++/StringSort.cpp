#include<iostream>
#include<vector>
#include<ctype.h>
using namespace std;

void StringSort(string& mystring){
    int length=mystring.length();
    bool flag=false;
    for(int i=length-1;i>0;i--){
        for(int j=0;j<i;j++){
            if(mystring[j]>mystring[j+1]){
                swap(mystring[j],mystring[j+1]);
                flag=true;
            }
        }
        if(!flag){
            break;
        }
    }
}

int main(){
    string mystring;
    cin>>mystring;
    StringSort(mystring);
    cout<<mystring;
}

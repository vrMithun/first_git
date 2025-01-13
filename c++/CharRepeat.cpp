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

string repeatcount(string& mystring){
    string test;
    int countt=0;
    int result=0;
    int length=mystring.length();
    for(int i=0;i<length-1;i++){
        if(mystring[i]==mystring[i+1]){
            countt++;
        }
        else if(result<countt){
            result=countt;
            countt=0;
            test=mystring[i];
        }
    }
    return test;
}


int main(){
    string mystring;
    cin>>mystring;
    StringSort(mystring);
    cout<<repeatcount(mystring);
}

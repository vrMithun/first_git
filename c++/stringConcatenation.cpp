#include <iostream>
#include <string>
using namespace std;

int main(){
    string s1="mithun ";
    string s2;
    getline(cin,s2);
    string s3=s1.append(s2);
    cout<<s3;
}

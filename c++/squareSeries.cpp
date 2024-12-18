#include <iostream>
using namespace std;

int main(){
    int n;
    int result=0;
    cout<<"Enter number of terms:";
    cin>> n;
    for(int i=1;i<n+1;i++){
        result+=i*i;
    }
    cout<<result;
}

#include <iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter number of terms:";
    cin>>n;
    int result=0;
    for(int i=0;i<n;i++){
        for(int j=1;j<=i+1;j++){
            result+=j;
        }
    }
    cout<<result;
}

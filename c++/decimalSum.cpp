#include <iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter number of terms:";
    cin>> n;
    float test=0;
    float result=0;
    for(int i=1;i<=n;i++){
        if (i>=9){
            test=i*100+(i+1);
            test/=100;
        }
        else{
            test=i*10+(i+1);
            test/=10;
        }
        cout<<test;
        cout<<" ";
        result+=test;
    }
    cout<<result;
}

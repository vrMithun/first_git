#include<iostream>
using namespace std;

double myPow(double x, int n) {
    double result=1;
    if(x==1){
        return 1;
    }
    if(n==0){
        return 1;
    }
    else if(n>0){
        for(int i=0;i<n;i++){
            result*=x;
            cout<<"priting when n>0";
        }
    }
    else{
        for(int i=n;i<0;i++){
            result/=x;
            cout<<"printing when n<0";
        }
    }
    return result;
}

int main(){
    cout<<myPow(2.0,-2);
}

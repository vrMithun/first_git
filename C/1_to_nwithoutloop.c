#include<stdio.h>
void print(int i,int n){
    if (i>n){
        return;
    }
    else{
        printf("%d ",i);
        print(i+1,n);
    }
}
int main(){
    print(1,10);
}


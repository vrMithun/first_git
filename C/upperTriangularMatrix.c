#include<stdio.h>
int main(){
    int arr[3][3]={{1,2,3},{0,6,7},{0,0,9}};
    int length=sizeof(arr)/sizeof(arr[0]);
    int test;
    for(int i=1;i<length;i++){
        for(int j=0;j<i;j++){
            if(arr[i][j]!=0){
                test=1;
            }
        }
    }
    if(test==1){
        printf("False");
    }
    else{
        printf("true");
    }
}

#include<stdio.h>
int main(){
    int arr[2][2]={{1,0},{0,1}};
    int test,i,j;
    int length=sizeof(arr)/sizeof(arr[0]);
    for( i=0;i<length;i++){
        for( j=0;j<length;j++){
            if(i==j && arr[i][j]==1){
                test++;
            }
            else if(i!=j && arr[i][j]==0){
                test++;
            }
            else{
                break;
            }
        }
    }
    if(test==length*length){
        printf("it is a unit matrix");
    }
    else{
        printf("it is not a unit matrix");
    }
}

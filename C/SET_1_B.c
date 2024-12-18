#include<stdio.h>
#include<stdlib.h>
void multi(int arr[],int length);
void sort(int *arr,int length);
int main(){
    int n;
    scanf("%d",&n);
    int *arr=(int *)malloc(n*sizeof(int));
    for(int i=0;i<n;i++){
        printf("Enter number %d:",i+1);
        scanf("%d",&arr[i]);
    }
    multi(arr,n);
    sort(arr,n);
    int positive=0;
    int zero=0;
    int productPositive=1;
    int productNegative=1;
    for(int j=0;j<n;j++){
        if(arr[j]<0){
            productNegative*=arr[j];
        }
        else if(arr[j]>0){
            positive++;
            productPositive*=arr[j];
        }
        else{
            zero++;
        }
    }
    if(productNegative<0){
        printf("minimum product is %d",productNegative*productPositive);
    }
    else{
        int product=1;
        for(int k=0;k<n-positive-zero-1;k++){
            if(arr[k]>=0){
                break;
            }
            else{
                product*=arr[k];
            }
        }
        printf("minimum product is %d",product*productPositive);

    }

}
void multi(int *arr,int length){
    int *arr2=(int *)malloc(length*sizeof(int));
    for(int i=0;i<length;i++){
        if(i==0 && length>2){
            arr2[i]=arr[i+1]*arr[i+2];
        }
        else if(i==length-1 && length>2){
            arr2[i]=arr[i-1]*arr[i-2];
        }
        else{
            arr2[i]=arr[i-1]*arr[i+1];
        }
        printf("%d ",arr2[i]);
    }
    printf("\n");
}
void sort(int *arr,int length){
    for(int i=0;i<length;i++){
        for(int j=0;j<length;j++){
            if(arr[j]>arr[j+1]){
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
}

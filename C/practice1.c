#include<stdio.h>
#include<stdlib.h>
int main(){
    int n;
    printf("Enter the length of array:");
    scanf("%d",&n);
    int *ptr=malloc(sizeof(*ptr));
    for(int i=0;i<n;i++){
        printf("Enter data:");
        scanf("%d",&ptr[i]);

    }
    for(int i=0;i<n;i++){
        printf("%d",ptr[i]);
    }
    free(ptr);
}

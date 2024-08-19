#include<stdio.h>
int main(){
    int i,j,n,t=1;
    scanf("%d",&n);
    for(i=0;i<=n;i++){
        for(j=1;j<=i;j++){
            printf("%d",t);
            t++;
        }
        printf("\n");
    }
}

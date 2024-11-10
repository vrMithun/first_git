#include<stdio.h>

int main(){
    FILE *file;
    file=fopen("mydataa.txt","a");

    if(file==NULL){
        printf("file not opened");
    }
    else{
        printf("file opened");
    }
    fclose(file);
}

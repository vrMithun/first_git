#include<stdio.h>
int main(){
    enum dayofweek{
        sunday=0,
        monday=0,
        tuesday,
        wednesday,
        thursday,
        friday,
        saturday      //enum values can be same but the names of the values must be different
    };
    enum dayofweek day=monday;
    /*day=monday;
    if(day==friday){
        printf("hi");
    }
    else{
        printf("hello");
    }*/
    printf("%d",day);
}

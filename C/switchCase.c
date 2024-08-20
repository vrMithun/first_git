#include<stdio.h>
int main(){
    char day;
    scanf("%c",&day);
    switch(day){
        case 1:
            printf("Monday");
            break;
        case 'a':
            printf("Tuesday");
            break;
        default:
            printf("invalid input");
            break;

    }
    return 0;
}
//rules for switch case
//default block is optional
//switch only accepts integer values
//break is optional
//duplicate case values are not allowed
//case value should be integer
//case value can be a operation
//switch case accepts character values

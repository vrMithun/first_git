#include<stdio.h>
typedef struct{
    char sname[20];
    int roll;
    float marks[5];
    float total;
    char grade;
}record;
void total(record s1[3]){
    for(int i=0;i<3;i++){
        float count=0;
        for(int j=0;j<5;j++){
            count=count+s1[i].marks[j];
        }
        printf("Mark of student %d=%f\n",i+1,count);
    }
}
int main(){
    record st[3];
    for(int i=0;i<3;i++){
        printf("Enter the mark of student %d:\n",i+1);
        for(int j=0;j<5;j++){
            printf("Enter Mark %d:",j+1);
            scanf("%f",&st[i].marks[j]);
        }
    }
    total(st);
}

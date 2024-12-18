#include<stdio.h>
#include<stdlib.h>
typedef struct{
    char name[30];
    int number;
    char country[30];
    int course;
    int goods;
    int domestic;
    int total;
}mystruct;

int main(){
    int n;
    printf("enter number of pilots:");
    scanf("%d",&n);
    mystruct PilotDetails[n];
    for(int i=0;i<n;i++){
        printf("enter name:");
        fgets(PilotDetails[i].name,sizeof(PilotDetails[i].name),stdin);
        getchar();
        printf("enter flight number:");
        scanf("%d",&PilotDetails[i].number);

        printf("enter country:");
        fgets(PilotDetails[i].country,sizeof(PilotDetails[i].country),stdin);
        getchar();
        printf("enter time(course):");
        scanf("%d",&PilotDetails[i].course);
        printf("enter time(goods):");
        scanf("%d",&PilotDetails[i].goods);
        printf("enter time(domestic):");
        scanf("%d",&PilotDetails[i].domestic);
        PilotDetails[i].total=PilotDetails[i].course+PilotDetails[i].goods+PilotDetails[i].domestic;
    }
}
void promotion(mystruct s[],int length){
    for(int i=0;i<length;i++){
        int total=s[i].course+s[i].goods+s[i].domestic;
        if(total>2000 && total<3000){
            printf("%s will get international goods aero pilot permit",s[i].name);

        }
        else if(total>3000){
            printf("%s will get international passenger aero pilot permit",s[i].name);
        }
    }
}
void sort(mystruct *s[],int length){
    for(int i=0;i<length;i++){
        for(int j=0;j<length;j++){

        }
    }
}

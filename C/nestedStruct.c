#include<stdio.h>
typedef struct{
        int year;
        int date;
        int month;
    }dob;
typedef struct{
    char name[30];//nested struct cant be used here directly as we only initialise a struct not declare.
    int roll;
    dob db;
    float cgpa;
}student;
void aboveCGPA(student s[3],int n){
    for(int i=0;i<3;i++){
        if (s[i].cgpa>n){
            printf("name:%s\nroll:%d\ndob:%d/%d/%d\ncgpa:%f\n\n",s[i].name,s[i].roll,s[i].db.date,s[i].db.month,s[i].db.year,s[i].cgpa);
        }
    }
}

void aboveDOB(student s[3],int n){
    for(int i=0;i<3;i++){
        if(s[i].db.year>n){
            printf("name:%s\nroll:%d\ndob:%d/%d/%d\ncgpa:%f\n\n",s[i].name,s[i].roll,s[i].db.date,s[i].db.month,s[i].db.year,s[i].cgpa);
        }
    }
}

void minCGPA(student s[3]){
    float *min=&s[0].cgpa;
    for (int i=1;i<5;i++){
        if(*min>s[i].cgpa){
            min=&s[i].cgpa;
        }
    }
    printf("%f",*min);
}

void sortCGPA(student s[3]){
    for(int i=0;i<3;i++){
        for(int j=0;j<2;j++){
            if(s[j].cgpa>s[j].cgpa){
                float temp=s[j].cgpa;
                s[j].cgpa=s[j+1].cgpa;
                s[j+1].cgpa=temp;
            }
        }
    }
    for(int i=0;i<3;i++){
        printf("%.2f\n",s[i].cgpa);
    }
}

int main(){
    student s[3];
    for(int i=0;i<3;i++){
        printf("Enter name: ");
        gets(s[i].name);

        printf("Enter roll number: ");
        scanf("%d", &s[i].roll);
        printf("Enter dob (day month year): ");
        scanf("%d %d %d", &s[i].db.date, &s[i].db.month, &s[i].db.year);

        printf("Enter CGPA: ");
        scanf("%f", &s[i].cgpa);
        getchar();
    }
    sortCGPA(s);
}

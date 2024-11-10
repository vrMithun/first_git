#include<stdio.h>
#include<string.h>
int main(){
    struct mystruct{
        char name[20];
        int roll_no;
        float cgpa;
    }person;
    strcpy(person.name,"joshua");
    printf("%s",person.name);
}

#include<stdio.h>
int main(){
    struct car{
        char model[20];
        int seat;
        float mileage;
    };
    struct car c;
    struct car *ptr=&c;
    //printf("%s %d %f\n",ptr->model,ptr->seat,ptr->mileage);
    //printf("%s %d %f",(*ptr).model,(*ptr).seat,(*ptr).mileage);

    scanf("%s %d %f",&ptr->model,&ptr->seat,&ptr->mileage);
    printf("%s %d %f",(*ptr).model,(*ptr).seat,(*ptr).mileage);
}

#include<stdio.h>
typedef struct{
    char name[20];
    int author_id;
}auth;

typedef struct{
    char title[30];
    auth author;
    int year;
    int price;
}book;

void viewBooks(book mybook[3]){
    for(int i=0;i<3;i++){
        printf("%s %s %d %d %d",mybook.title,mybook.author.name,mybook.author.author_id,)
    }
}
int main(){
    book mybook[3];

}

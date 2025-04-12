#include<iostream>
#include<vector>
using namespace std;

class Animal{
protected:
    string name;
public:
    Animal(string animal){
        name=animal;
    }
    virtual void makeSound(){
        cout<<"roar\n";
    }
};

class Dog:public Animal{
public:
    Dog(string animal) : Animal(animal) {}
    void makeSound() override{
        cout<<"bark!\n";
    }
};


int main(){
    Dog myobj("mydog");
    myobj.makeSound();
}

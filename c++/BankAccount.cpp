#include<iostream>
#include<vector>
using namespace std;

class BankAccount{
private:
    int accountNumber;
    double balance;

public:
    BankAccount(int accnum,int bal){
        accountNumber=accnum;
        balance=bal;
    }
    void deposit(double amount){
        if(amount>0){
            balance+=amount;
        }
        else cout<<"invalid deposit"<<"\n";
    }
    void withdraw(double amount){
        if(balance>amount){
            balance-=amount;
            cout<<"money deducted\n";
        }
        else cout<<"insufficient balance\n";
    }
    void display(){
        cout<<"account number:"<<accountNumber<<"\n";
        cout<<"current balance:"<<balance<<"\n";
    }
};

int main(){
    BankAccount myobj(123,1000);
    myobj.deposit(100);
    myobj.display();
    myobj.withdraw(200);
    myobj.display();
    myobj.withdraw(1000);
    myobj.display();
}

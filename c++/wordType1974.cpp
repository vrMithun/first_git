#include<iostream>
#include<vector>
#include<cstdlib>
using namespace std;

int minTime(string word){
    int time=0;
    char start='a';
    int ascii_curr=int(start);
    for(char mychar:word){
        int ascii_next=int(mychar);
        int diff=abs(ascii_curr-ascii_next);
        if(diff==0){
            time++;
        }
        else if(diff>13){
            time+=26-diff+1;
        }
        else{
            time+=diff+1;
        }
        ascii_curr=ascii_next;
    }
    return time;
}

int main(){
    string word="bza";
    cout<<minTime(word);
}

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int birthdaycake(vector<int>& candles){
    if(candles.size()==1){
        return 1;
    }
    priority_queue<int> pq;
    for(int i=0;i<candles.size();i++){
        pq.push(candles.at(i));
    }
    int mycount=0;
    while(!pq.empty()){
        int first=pq.top();
        pq.pop();
        int second=pq.top();
        if(first==second){
            mycount++;
        }
    }
    return mycount;
}

int main(){
    vector<int> candles={4,1,3,4};
    cout<<birthdaycake(candles);
}

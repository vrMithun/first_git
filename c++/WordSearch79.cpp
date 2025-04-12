#include<iostream>
#include<vector>
using namespace std;

bool helper(vector<vector<char>>& board,vector<int>& myvect,vector<bool>& visited,int length,int mycount,string word);

bool exist(vector<vector<char>>& board, string word) {
    vector<vector<int>> index;
    for(int i=0;i<board.size();i++){
        for(int j=0;j<board.at(0).size();j++){
            if(board.at(i).at(j)==word[0]){
                index.push_back({i,j});
            }
        }
    }
    int length=index.size();
    for(vector<int> i:index){
        vector<bool> visited(word.size(),false);
        helper(board,i,visited,length,1,word);
    }
}

bool helper(vector<vector<char>>& board,vector<int>& myvect,vector<bool>& visited,int length,int mycount,string word){
    if(length<mycount){
        return true;
    }
    int row=myvect.at(0);
    int column=myvect.at(1);
}

int main(){
    vector<vector<char>> board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    string word = "ABCCED";
}

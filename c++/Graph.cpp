#include<iostream>
#include<vector>
#include<queue>

using namespace std;

void add_node(vector<char>& vectnode,char node){
    vectnode.push_back(node);
}

int getNode_index(vector<char>& vectnode, char node){
    for(int i=0;i<vectnode.size();i++){
        if(vectnode.at(i)==node){
            return i;
        }
    }
    return -1;
}

void add_edge(vector<vector<char>>& myvect,vector<char>& vectnode,char parent,char child){
    int parentIndex=getNode_index(vectnode,parent);
    int childIndex=getNode_index(vectnode,child);
    myvect[parentIndex].push_back(child);
    myvect[childIndex].push_back(parent);
}

void display_graph(vector<vector<char>>& myvect,vector<char>& vectnode){
    int length=vectnode.size();
    for(int i=0;i<length;i++){
        cout<<vectnode.at(i)<<"->";
        for(int j=0;j<myvect[i].size();j++){
            cout<<myvect[i].at(j)<<" ";
        }
        cout<<"\n";
    }
}

void dfs_helper(vector<vector<char>>& myvect,vector<bool>& is_visited,vector<char>& vectnode,int current_index){

    is_visited.at(current_index)=true;
    cout<<vectnode.at(current_index)<<" ";
    for(char i:myvect[current_index]){
        int index=getNode_index(vectnode,i);
        if(!is_visited.at(index)){
            dfs_helper(myvect,is_visited,vectnode,index);
        }
    }
}

void dfs(vector<vector<char>>& myvect,vector<char>& vectnode,char start){
    int start_index=getNode_index(vectnode,start);
    vector<bool> is_visited;
    for(int i=0;i<vectnode.size();i++){
        is_visited.push_back(false);
    }

    dfs_helper(myvect,is_visited,vectnode,start_index);


}

void bfs(vector<vector<char>>& myvect, vector<char>& vectnode,char startnode){
    queue<char> myqueue;
    myqueue.push(startnode);
    vector<bool> is_visited;
    for(int i=0;i<vectnode.size();i++){
        is_visited.push_back(false);
    }
    int Start_index=getNode_index(vectnode,startnode);
    is_visited[Start_index]=true;
    while(!myqueue.empty()){
        char temp=myqueue.front();
        myqueue.pop();
        cout<<temp<<" ";
        int index=getNode_index(vectnode,temp);

        for(char i:myvect[index]){
            int tempIndex=getNode_index(vectnode,i);
            if(!is_visited.at(tempIndex)){
                myqueue.push(i);
                is_visited.at(tempIndex)=true;
            }
        }
    }
}

bool cycle_helper(vector<vector<char>>& myvect,vector<bool>& is_visited,vector<char>& vectnode,vector<int>& parent,int current_index){
    is_visited.at(current_index)=true;
    for(char i:myvect[current_index]){
        int index=getNode_index(vectnode,i);
        if(!is_visited.at(index)){
            parent.at(index)=current_index;
            if (cycle_helper(myvect, is_visited, vectnode, parent, index)) {
                return true;
            }
        }
        else if(parent.at(current_index)!=index){
            return true;
        }
    }
    return false;
}

void cycle(vector<vector<char>>& myvect,vector<char>& vectnode,char start){
    int start_index=getNode_index(vectnode,start);
    vector<bool> is_visited;
    for(int i=0;i<vectnode.size();i++){
        is_visited.push_back(false);
    }
    vector<int> parent(vectnode.size(),-1);
    cout<<cycle_helper(myvect,is_visited,vectnode,parent,start_index);


}

int main(){
    vector<char> vectnode;
    add_node(vectnode,'A');
    add_node(vectnode,'B');
    add_node(vectnode,'C');
    add_node(vectnode,'D');
    add_node(vectnode,'E');

    vector<vector<char>> myvect(vectnode.size());
    add_edge(myvect,vectnode,'A','B');
    add_edge(myvect,vectnode,'A','C');
    add_edge(myvect,vectnode,'B','D');
    add_edge(myvect,vectnode,'C','E');
    add_edge(myvect,vectnode,'D','E');

    //display_graph(myvect,vectnode);

    //dfs(myvect,vectnode,'A');
    //bfs(myvect,vectnode,'A');
    cycle(myvect,vectnode,'A');
}

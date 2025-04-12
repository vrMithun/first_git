#include<iostream>
#include<vector>
#include<queue>
#include<math.h>
using namespace std;

int get_index(vector<char>& vertices,char vertex){
    for(int i=0;i<vertices.size();i++){
        if(vertices.at(i)==vertex){
            return i;
        }
    }
    return -1;
}

void add_edges(vector<vector<int>>& matrix,vector<char>& vertices,char edge1,char edge2,int weight){
    int edge1_index=get_index(vertices,edge1);
    int edge2_index=get_index(vertices,edge2);
    if(edge1_index!=-1 && edge2_index!=-1){
        matrix[edge1_index][edge2_index]=weight;
        matrix[edge2_index][edge1_index]=weight;
    }
}

void display_matrix(vector<vector<int>>& matrix){
    for(int i=0;i<matrix.size();i++){
        for(int j=0;j<matrix.size();j++){
            cout<<matrix[i][j]<<" ";
        }
        cout<<"\n";
    }
}

int dijkstra(vector<vector<int>>& matrix,vector<char>& vertices,char start,char endnode){
    vector<bool> is_visited(matrix.size(),false);
    int start_index=get_index(vertices,start);
    int end_index=get_index(vertices,endnode);
    vector<int> distance(matrix.size(),100000);
    distance.at(start_index)=0;
    while(1){
        int min_distance=100000;
        int node_index=-1;
        for(int i=0;i<matrix.size();i++){
            if(!is_visited.at(i) && min_distance>distance.at(i)){
                min_distance=distance.at(i);
                node_index=i;
            }
        }
        if(node_index==-1){
            break;
        }
        is_visited.at(node_index)=true;

        for(int i=0;i<matrix.size();i++){
            if(matrix.at(node_index).at(i)!=100000 && !is_visited.at(i)){
                int new_distance=distance.at(node_index)+matrix.at(node_index).at(i);
                if(new_distance<distance.at(i)){
                    distance.at(i)=new_distance;
                }
            }
        }
    }
    return distance.at(end_index);
}

int main(){
    vector<char> vertices={'A','B','C','D','E'};
    vector<vector<int>> matrix(5, vector<int>(5, 100000));
    add_edges(matrix,vertices,'A','B',3);
    add_edges(matrix,vertices,'A','C',5);
    add_edges(matrix,vertices,'E','B',4);
    add_edges(matrix,vertices,'C','E',2);
    add_edges(matrix,vertices,'D','E',5);
    add_edges(matrix,vertices,'D','C',7);

    //display_matrix(matrix);
    cout<<dijkstra(matrix,vertices,'B','C');
}

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Graph {
    int V;
    vector<vector<int>> adj;  // Adjacency list
    vector<vector<int>> revAdj;  // Transposed graph

public:
    Graph(int V) {
        this->V = V;
        adj.resize(V);
        revAdj.resize(V);
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        revAdj[v].push_back(u);  // Reverse edge for transpose
    }

    void DFS(int v, vector<bool>& visited, stack<int>& finishStack) {
        visited[v] = true;
        for (int neighbor : adj[v]) {
            if (!visited[neighbor])
                DFS(neighbor, visited, finishStack);
        }
        finishStack.push(v);  // Store vertex in stack based on finish time
    }

    void reverseDFS(int v, vector<bool>& visited) {
        visited[v] = true;
        cout << v << " ";  // Print the component
        for (int neighbor : revAdj[v]) {
            if (!visited[neighbor])
                reverseDFS(neighbor, visited);
        }
    }

    void findSCCs() {
        stack<int> finishStack;
        vector<bool> visited(V, false);

        // Step 1: Perform DFS and store finish order
        for (int i = 0; i < V; i++) {
            if (!visited[i])
                DFS(i, visited, finishStack);
        }

        // Step 2: Transpose graph is already stored in revAdj

        // Step 3: Perform DFS on transposed graph
        fill(visited.begin(), visited.end(), false);

        cout << "Strongly Connected Components:\n";
        while (!finishStack.empty()) {
            int v = finishStack.top();
            finishStack.pop();
            if (!visited[v]) {
                reverseDFS(v, visited);
                cout << endl;
            }
        }
    }
};

int main() {
    Graph g(5);
    g.addEdge(1, 0);
    g.addEdge(0, 2);
    g.addEdge(2, 1);
    g.addEdge(0, 3);
    g.addEdge(3, 4);

    g.findSCCs();
    return 0;
}


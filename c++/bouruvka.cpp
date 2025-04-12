#include <iostream>
#include <vector>
#include <climits>

using namespace std;

struct Edge {
    int src, dest, weight;
};

struct Graph {
    int V, E;
    vector<Edge> edges;

    Graph(int V, int E) {
        this->V = V;
        this->E = E;
    }

    void addEdge(int src, int dest, int weight) {
        edges.push_back({src, dest, weight});
    }
};

int findParent(vector<int>& parent, int i) {
    if (parent[i] != i)
        parent[i] = findParent(parent, parent[i]);
    return parent[i];
}

void unionSets(vector<int>& parent, vector<int>& rank, int u, int v) {
    int rootU = findParent(parent, u);
    int rootV = findParent(parent, v);

    if (rootU != rootV) {
        if (rank[rootU] < rank[rootV]) {
            parent[rootU] = rootV;
        } else if (rank[rootU] > rank[rootV]) {
            parent[rootV] = rootU;
        } else {
            parent[rootV] = rootU;
            rank[rootU]++;
        }
    }
}

void boruvkaMST(Graph& graph) {
    int V = graph.V;
    vector<int> parent(V), rank(V, 0);

    for (int i = 0; i < V; i++)
        parent[i] = i;

    int MST_weight = 0, components = V;

    while (components > 1) {
        vector<int> cheapest(V, -1);

        for (int i = 0; i < graph.E; i++) {
            int u = findParent(parent, graph.edges[i].src);
            int v = findParent(parent, graph.edges[i].dest);

            if (u != v) {
                if (cheapest[u] == -1 || graph.edges[i].weight < graph.edges[cheapest[u]].weight)
                    cheapest[u] = i;

                if (cheapest[v] == -1 || graph.edges[i].weight < graph.edges[cheapest[v]].weight)
                    cheapest[v] = i;
            }
        }

        for (int i = 0; i < V; i++) {
            if (cheapest[i] != -1) {
                int u = graph.edges[cheapest[i]].src;
                int v = graph.edges[cheapest[i]].dest;
                int weight = graph.edges[cheapest[i]].weight;

                int setU = findParent(parent, u);
                int setV = findParent(parent, v);

                if (setU != setV) {
                    cout << "Edge added: " << u << " - " << v << " (Weight: " << weight << ")\n";
                    MST_weight += weight;
                    unionSets(parent, rank, setU, setV);
                    components--;
                }
            }
        }
    }

    cout << "Total MST weight: " << MST_weight << endl;
}

int main() {
    int V = 6, E = 9;
    Graph graph(V, E);

    graph.addEdge(0, 1, 4);
    graph.addEdge(0, 2, 4);
    graph.addEdge(1, 2, 2);
    graph.addEdge(1, 3, 5);
    graph.addEdge(2, 3, 5);
    graph.addEdge(2, 4, 3);
    graph.addEdge(3, 4, 2);
    graph.addEdge(3, 5, 6);
    graph.addEdge(4, 5, 7);

    boruvkaMST(graph);
    return 0;
}


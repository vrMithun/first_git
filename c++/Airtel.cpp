#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

// Structure to represent a node
struct Node {
    int id;
    string label;
    string country;
    double longitude;
    double latitude;
    bool internal;
};

// Structure to represent an edge
struct Edge {
    int source;
    int target;
    string linkLabel;
    double weight; // Added for weighted algorithms
};

// Graph class
class Graph {
private:
    unordered_map<int, Node> nodes; // Node ID to Node mapping
    unordered_map<int, vector<Edge>> adjacencyList; // Adjacency list for edges

public:
    // Add a node to the graph
    void addNode(int id, const string &label, const string &country, double longitude, double latitude, bool internal) {
        Node node = {id, label, country, longitude, latitude, internal};
        nodes[id] = node;
    }

    // Add an edge to the graph
    void addEdge(int source, int target, const string &linkLabel, double weight = 1.0) {
        Edge edge = {source, target, linkLabel, weight};
        adjacencyList[source].push_back(edge);
    }

    // Display the graph
    void displayGraph() {
        cout << "Nodes:" << endl;
        for (const auto &pair : nodes) {
            const Node &node = pair.second;
            cout << "ID: " << node.id << ", Label: " << node.label;
            if (!node.country.empty()) {
                cout << ", Country: " << node.country;
            }
            cout << ", Longitude: " << node.longitude << ", Latitude: " << node.latitude;
            cout << ", Internal: " << (node.internal ? "Yes" : "No") << endl;
        }

        cout << "\nEdges:" << endl;
        for (const auto &pair : adjacencyList) {
            int source = pair.first;
            for (const Edge &edge : pair.second) {
                cout << "Source: " << source << ", Target: " << edge.target;
                if (!edge.linkLabel.empty()) {
                    cout << ", LinkLabel: " << edge.linkLabel;
                }
                cout << ", Weight: " << edge.weight << endl;
            }
        }
    }

    // Create adjacency matrix
    vector<vector<double>> createAdjacencyMatrix() {
        int n = nodes.size();
        vector<vector<double>> adjMatrix(n, vector<double>(n, 1e9));
        for (int i = 0; i < n; i++) adjMatrix[i][i] = 0;

        for (const auto &pair : adjacencyList) {
            int source = pair.first;
            for (const Edge &edge : pair.second) {
                adjMatrix[source][edge.target] = edge.weight;
            }
        }

        return adjMatrix;
    }

    // Depth-First Search
    void DFS(int start) {
        unordered_map<int, bool> visited;
        stack<int> s;
        s.push(start);

        cout << "DFS Traversal: ";
        while (!s.empty()) {
            int current = s.top();
            s.pop();

            if (!visited[current]) {
                cout << current << " ";
                visited[current] = true;
            }

            for (const Edge &edge : adjacencyList[current]) {
                if (!visited[edge.target]) {
                    s.push(edge.target);
                }
            }
        }
        cout << endl;
    }

    // Breadth-First Search
    void BFS(int start) {
        unordered_map<int, bool> visited;
        queue<int> q;
        q.push(start);
        visited[start] = true;

        cout << "BFS Traversal: ";
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            cout << current << " ";

            for (const Edge &edge : adjacencyList[current]) {
                if (!visited[edge.target]) {
                    q.push(edge.target);
                    visited[edge.target] = true;
                }
            }
        }
        cout << endl;
    }

    // Dijkstra's algorithm
    void dijkstra(int source) {
        unordered_map<int, double> distances;
        for (const auto &node : nodes) {
            distances[node.first] = 1e9;
        }
        distances[source] = 0;

        priority_queue<pair<double, int>, vector<pair<double, int>>, greater<>> pq;
        pq.push({0, source});

        while (!pq.empty()) {
            auto [dist, current] = pq.top();
            pq.pop();

            for (const Edge &edge : adjacencyList[current]) {
                double newDist = dist + edge.weight;
                if (newDist < distances[edge.target]) {
                    distances[edge.target] = newDist;
                    pq.push({newDist, edge.target});
                }
            }
        }

        cout << "Dijkstra's Shortest Path from Node " << source << ":" << endl;
        for (const auto &pair : distances) {
            cout << "Node " << pair.first << ": " << pair.second << endl;
        }
    }

    // Kruskal's algorithm for Minimum Spanning Tree
    void kruskal() {
        struct Subset {
            int parent;
            int rank;
        };

        unordered_map<int, Subset> subsets;
        for (const auto &node : nodes) {
            subsets[node.first] = {node.first, 0};
        }

        auto customFind = [&](int u) {
            while (u != subsets[u].parent) {
                subsets[u].parent = subsets[subsets[u].parent].parent; // Path compression
                u = subsets[u].parent;
            }
            return u;
        };

        auto unionSet = [&](int u, int v) {
            int rootU = customFind(u);
            int rootV = customFind(v);

            if (subsets[rootU].rank < subsets[rootV].rank) {
                subsets[rootU].parent = rootV;
            } else if (subsets[rootU].rank > subsets[rootV].rank) {
                subsets[rootV].parent = rootU;
            } else {
                subsets[rootV].parent = rootU;
                subsets[rootU].rank++;
            }
        };

        vector<Edge> edges;
        for (const auto &pair : adjacencyList) {
            for (const Edge &edge : pair.second) {
                edges.push_back(edge);
            }
        }

        sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b) {
            return a.weight < b.weight;
        });

        double mstWeight = 0;
        for (const Edge &edge : edges) {
            int rootU = customFind(edge.source);
            int rootV = customFind(edge.target);

            if (rootU != rootV) {
                mstWeight += edge.weight;
                unionSet(edge.source, edge.target);
            }
        }

        cout << "Minimum Spanning Tree Weight (Kruskal's): " << mstWeight << endl;
    }
};
int main() {
    Graph graph;

    // Adding nodes
    graph.addNode(0, "Los Angeles", "United States", -118.24368, 34.05223, true);
    graph.addNode(1, "Chennai", "India", 80.27847, 13.08784, true);
    graph.addNode(2, "NYIX", "", 0, 0, false);
    graph.addNode(3, "LAIX", "", 0, 0, false);
    graph.addNode(4, "NiXI", "", 0, 0, false);
    graph.addNode(5, "LINX", "", 0, 0, false);
    graph.addNode(6, "AMSIX", "", 0, 0, false);

    // Adding edges
    graph.addEdge(0, 2, "Link1", 5.0);
    graph.addEdge(1, 4, "Link2", 3.0);
    graph.addEdge(2, 3, "Link3", 2.0);
    graph.addEdge(3, 5, "Link4", 6.0);
    graph.addEdge(4, 6, "Link5", 1.0);
    graph.addEdge(5, 6, "Link6", 4.0);

    // Displaying the graph
    graph.displayGraph();

    // Traversal and algorithms
    graph.DFS(0);
    graph.BFS(0);
    graph.dijkstra(0);
    graph.kruskal();

    return 0;
}

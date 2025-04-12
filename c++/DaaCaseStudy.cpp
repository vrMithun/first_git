#include <iostream>
#include <vector>
#include <limits>
#include <unordered_map>
using namespace std;

struct Edge {
    int from, to, weight;
};

class ChuLiuEdmonds {
public:
    int n;
    vector<Edge> edges;

    ChuLiuEdmonds(int nodes) : n(nodes) {}

    void addEdge(int u, int v, int w) {
        edges.push_back({u, v, w});
    }

    int findMaxArborescence(int root) {
        vector<int> parent(n, -1), minEdge(n, numeric_limits<int>::max());
        vector<int> cycle(n, -1);
        vector<bool> visited(n, false);
        vector<Edge> minIncomingEdge(n);
        int totalWeight = 0;

        cout << "Finding minimum incoming edges for each node:\n";
        for (const auto& edge : edges) {
            if (edge.to != root && edge.weight < minEdge[edge.to]) {
                minEdge[edge.to] = edge.weight;
                parent[edge.to] = edge.from;
                minIncomingEdge[edge.to] = edge;
            }
        }

        for (int i = 0; i < n; ++i) {
            if (i != root && parent[i] != -1) {
                cout << "Node " << i << " gets minimum edge from " << parent[i] << " with weight " << minEdge[i] << "\n";
            }
        }

        cout << "Checking for cycles:\n";
        for (int i = 0; i < n; ++i) {
            if (i == root || visited[i]) continue;
            int current = i;
            unordered_map<int, bool> cycleMap;
            while (current != -1 && !visited[current]) {
                visited[current] = true;
                cycleMap[current] = true;
                current = parent[current];
            }

            if (current != -1 && cycleMap.count(current)) {
                int cycleStart = current;
                cout << "Cycle detected starting at node " << cycleStart << "\n";
                do {
                    cycle[current] = cycleStart;
                    cout << "Node " << current << " is in cycle." << "\n";
                    current = parent[current];
                } while (current != cycleStart);
            }
        }

        cout << "Calculating total weight of maximum arborescence:\n";
        for (int i = 0; i < n; ++i) {
            if (i != root && cycle[i] == -1 && parent[i] != -1) {
                totalWeight += minEdge[i];
                cout << "Including edge (" << parent[i] << " -> " << i << ") with weight " << minEdge[i] << "\n";
            }
        }

        cout << "Edges in Maximum Arborescence:\n";
        for (int i = 0; i < n; ++i) {
            if (parent[i] != -1) {
                cout << "(" << parent[i] << " -> " << i << ") Weight: " << minEdge[i] << "\n";
            }
        }

        return totalWeight;
    }
};

int main() {
    int nodes = 5; // Example with 5 nodes
    ChuLiuEdmonds algorithm(nodes);

    algorithm.addEdge(0, 1, 1);
    algorithm.addEdge(0, 2, 2);
    algorithm.addEdge(1, 3, 3);
    algorithm.addEdge(2, 3, 4);
    algorithm.addEdge(3, 4, 5);
    algorithm.addEdge(2, 4, 6);

    int root = 0;
    int maxArborescenceWeight = algorithm.findMaxArborescence(root);

    cout << "Total weight of Maximum Arborescence: " << maxArborescenceWeight << "\n";
    return 0;
}

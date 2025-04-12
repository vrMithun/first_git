class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def prims_algorithm(self,Start):
        start_index=self.vertex_data.index(Start)
        in_mst=[False]*self.size
        parent=[-1]*self.size
        key_val=[float('inf')]*self.size
        key_val[start_index]=0
        for _ in range(self.size):
            min_val=float('inf')
            u=-1
            for i in range(self.size):
                if not in_mst[i] and key_val[i]<min_val:
                    min_val=key_val[i]
                    u=i

            in_mst[u]=True
            if parent[u]!=-1:
                print(self.vertex_data[parent[u]], self.vertex_data[u])

            for j in range(self.size):
                if 0<self.adj_matrix[u][j]<key_val[j] and not in_mst[j]:
                    key_val[j]=self.adj_matrix[u][j]
                    parent[j]=u


g = Graph(8)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
g.add_vertex_data(7, 'H')

g.add_edge(0, 1, 3)  # A - B
g.add_edge(0, 3, 4)  # A - D
g.add_edge(1, 2, 3)  # B - C
g.add_edge(1, 3, 5)  # B - D
g.add_edge(1, 4, 6)  # B - E
g.add_edge(2, 4, 4)  # C - E
g.add_edge(2, 7, 2)  # C - H
g.add_edge(3, 4, 7)  # D - E
g.add_edge(3, 5, 4)  # D - F
g.add_edge(4, 5, 5)  # E - F
g.add_edge(4, 6, 3)  # E - G
g.add_edge(5, 6, 7)  # F - G
g.add_edge(6, 7, 5)  # G - H

print("Prim's Algorithm MST:")
g.prims_algorithm('A')
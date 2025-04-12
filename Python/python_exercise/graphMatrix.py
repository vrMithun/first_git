class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
    def util(self,index,visited):
        visited[index]=True
        print(self.vertex_data[index])
        for i in range(self.size):
            if self.adj_matrix[index][i]==1 and not visited[i]:
                self.util(i,visited)
    def dfs(self,Start):
        StartIndex=self.vertex_data.index(Start)
        visited=[False]*self.size
        self.util(StartIndex,visited)

    def bfs(self,Start):
        queue=[self.vertex_data.index(Start)]
        visited=[False]*self.size
        visited[queue[0]]=True
        while queue:
            index=queue.pop(0)
            print(self.vertex_data[index])
            for i in range(self.size):
                if not visited[i] and self.adj_matrix[index][i]==1:
                    queue.append(i)
                    visited[i]=True
    def util2(self,index,visited,parent):
        visited[index]=True
        for i in range(self.size):
            if self.adj_matrix[index][i]==1:
                if not visited[i]:
                    if self.util2(i,visited,index):
                        return True
                elif parent!=i:
                    return True
        return False        
                
    def is_cycle(self):
        visited=[False]*self.size
        for i in range(self.size):
            if not visited[i]:
                if self.util2(i,visited,-1):
                    return True
        return False        

    def shortest_path(self,Start):
        start_vertex=self.vertex_data.index(Start)
        visited=[False]*self.size
        distances=[float('inf')]*self.size
        distances[start_vertex]=0

        for _ in range(self.size):
            min_dis=float('inf')
            u=None
            for i in range(self.size):
                if not visited[i] and distances[i]<min_dis:
                    min_dis=distances[i]
                    u=i
            if u==None:
                return None
            visited[u]=True
            for j in range(self.size):
                if not visited[j] and self.adj_matrix[u][j]!=0:
                    alt=distances[u]+self.adj_matrix[u][j]
                    if alt < distances[j]:
                        distances[j] = alt
        print(distances)
g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.shortest_path('A')
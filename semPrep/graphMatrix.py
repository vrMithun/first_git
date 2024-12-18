class Graph:
    def __init__(self,size):
        self.size=size
        self.mat=[[0]*self.size for _ in range(self.size)]
        self.vertex_data=['']*self.size

    def add_vertex_data(self,index,data):
        if index<self.size:
            self.vertex_data[index]=data

    def add_edge(self,v1,v2,weight):
        self.mat[v1][v2]=weight
        #self.mat[v2][v1]=weight

    def display(self):
        for i in range(self.size):
            print(" ".join(map(str,self.mat[i])))

    def util(self,index,visited):
        visited[index]=True
        print(self.vertex_data[index])
        for i in range(self.size):
            if self.mat[index][i]>0 and not visited[i]:
                self.util(i,visited)

    def dfs(self,Start):
        visited=[False]*self.size
        Start_vertex=self.vertex_data.index(Start)
        self.util(Start_vertex,visited)

    def bfs(self,Start):
        visited=[False]*self.size
        heap=[]
        start_vertex=self.vertex_data.index(Start)
        visited[start_vertex]=True
        heap.append(start_vertex)
        while heap:
            print(self.vertex_data[heap[0]])
            v=heap.pop(0)
            for i in range(self.size):
                if self.mat[v][i]>0 and not visited[i]:
                    heap.append(i)
                    visited[i]=True

    def util2(self,index,visited,stack):
        visited[index]=True
        stack[index]=True
        for i in range(self.size):
            if self.mat[index][i]>0:
                if not visited[i]:
                    if self.util2(i,visited,stack):
                        return True
                elif stack[i]:
                    return True 
        stack[index]=False           
        return False
    def is_cycle(self):
        visited=[False]*self.size
        stack=[False]*self.size
        for i in range(self.size):
            if not visited[i]:
                if self.util2(i,visited,stack):
                    return True
        return False
g=Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(0, 1, 4)  # A-B,  4
g.add_edge(0, 6, 10) # A-G, 10
g.add_edge(0, 2, 9)  # A-C,  9
g.add_edge(1, 2, 8)  # B-C,  8
g.add_edge(2, 3, 5)  # C-D,  5
g.add_edge(2, 4, 2)  # C-E,  2
g.add_edge(2, 6, 7)  # C-G,  7
g.add_edge(3, 4, 3)  # D-E,  3
g.add_edge(3, 5, 7)  # D-F,  7
g.add_edge(4, 6, 6)  # E-G,  6
g.add_edge(5, 6, 11) # F-G, 11

print(g.is_cycle())
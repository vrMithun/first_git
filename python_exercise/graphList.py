class Graph:
    def __init__(self,size):
        self.size=size
        self.vertex=[[] for _ in range (self.size)]
        self.vertex_data=['']*size
        

    def add_edge(self,start,end):
        u=self.vertex_data.index(start)    
        v=self.vertex_data.index(end)
        self.vertex[u].append(end)
        self.vertex[v].append(start)

    def add_vertex(self,index,data):
        self.vertex_data[index]=data    

    def display(self):
        for i in range(len(self.vertex_data)):
            print(self.vertex_data[i],'->',end=' ')
            for j in self.vertex[i]:
                print(j,end=' ')
            print()    

myobj=Graph(4)
myobj.add_vertex(0,'a')
myobj.add_vertex(1,'b')
myobj.add_vertex(2,'c')
myobj.add_vertex(3,'d')
myobj.add_edge('a','b')
myobj.add_edge('a','c')
myobj.add_edge('d','b')
myobj.add_edge('d','a')
myobj.display()
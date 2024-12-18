class Graph:
    def __init__(self,size):
        self.mat=[[] for _ in range(size)]
        self.vertex=['']*size
        self.size=size
    def vert(self,index,data):
        if 0<=index<self.size  and data:
            self.vertex[index]=data
    def edge(self,start,end):
        vertStart=self.vertex.index(start)
        vertEnd=self.vertex.index(end)
        self.mat[vertStart].append(end)
        self.mat[vertEnd].append(start)

    def display(self):
        for i in range(self.size):
            print(self.vertex[i],"->",end=" ")
            for j in range(len(self.mat[i])):
                print(self.mat[i][j],end=" ")
            print()
myobj=Graph(5)
myobj.vert(0,'A')
myobj.vert(1,'B')
myobj.vert(2,'C')
myobj.vert(3,'D')
myobj.vert(4,'E')

myobj.edge('A','B')
myobj.edge('A','C')
myobj.edge('C','B')
myobj.edge('D','B')
myobj.edge('A','D')
myobj.edge('C','D')
myobj.display()
class Heap:
    def __init__(self):
        self.heap=[None]
    def add(self,tuple):
        self.heap.append(tuple)
        self.upheap(len(self.heap)-1)
    def upheap(self,index):
        parent=index//2
        while parent>0 and self.heap[index][0]>self.heap[parent][0]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            index=parent
            parent=index//2
    def min(self):
        temp2=self.heap[1]
        temp=self.heap.pop()
        self.heap[1]=temp
        self.downheap(1)
        return temp2
    def downheap(self,index):
        left=index*2
        right=index*2+1
        smallest=index
        if left<len(self.heap) and self.heap[smallest][0]<self.heap[left][0]:
            smallest=left
        if right<len(self.heap) and self.heap[smallest][0]<self.heap[right][0]:
            smallest=right
        if smallest!=index:
            self.heap[smallest],self.heap[index]=self.heap[index],self.heap[smallest]
            self.downheap(smallest)
    def getHeap(self):
        print(self.heap)
    def kth(self,num):
        for _ in range(num-1):
            self.min()
        print(self.min())    
myobj=Heap()
myobj.add((8,'a'))
myobj.add((2,'b'))
myobj.add((7,'c'))
myobj.add((4,'g'))
myobj.kth(3)
myobj.getHeap()

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None

class Heap:
    def __init__(self):
        self.root=None
        self.height=0
    def BuiltTree(self,arr):
        self.address=[None]
        for i in range(1,len(arr)):
            if arr[i]!=-1:
                new_node=Node(arr[i])
                self.address.append(new_node) 
                if i!=1:
                    new_node.parent=self.address[i//2]
                    if i%2==0:
                        self.address[i//2].left=new_node
                    else:
                        self.address[i//2].right=new_node    
                 
        self.root=self.address[1]        
        self.size=len(arr)
    def Preorder(self):
        result=[]
        if self.root==None:
            return None
        def traverse(n):
            if n:
                result.append(n.data)
                traverse(n.left)
                traverse(n.right)
        traverse(self.root)
        print(result)

    def Heapify(self,root):
        if root is None:
            return
        smallest=root
        if root.left and root.left.data<smallest.data:
            smallest=root.left
        if root.right and root.right.data<smallest.data:
            smallest=root.right
        if smallest!=root:
            smallest.data,root.data=root.data,smallest.data
            self.Heapify(smallest)          
    def Heap(self): 
        n=self.root
        def traversal(root):
            if root==None:
                return
            if root.left:
                traversal(root.left)
            if root.right:
                traversal(root.right)
            self.Heapify(root)
        traversal(n)
    def Height(self):
        root=self.root
        while root.left:
            root=root.left 
            self.height+=1
        return self.height    
               
    def add(self,value):
        index=2**(self.height)
        i=2**(self.height-1)
        while i<index:
            new_Node=Node(value)
            if self.address[i].left==None:
                self.address[i].left=new_Node
                new_Node.parent=self.address[i]
                break
            elif self.address[i].right==None:
                self.address[i].right=new_Node
                new_Node.parent=self.address[i]
                break
            i+=1

myobj=Heap()
myobj.BuiltTree([0,21,10,30,5,12,25,100,3,7]) 
myobj.Heap()       
myobj.Preorder()
print(myobj.Height())
myobj.add(6)
myobj.Preorder()
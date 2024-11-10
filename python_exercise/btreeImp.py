class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def BuildTree(self,lst):
        address=[None]
        for i in range(1,len(lst)):
            if lst[i]!=-1:
                temp=Node(lst[i])
                address.append(temp)
                if i!=1:
                    temp.parent=address[i//2]
                    if i%2==0:
                        temp.parent.left=address[i]
                    else:
                        temp.parent.right=address[i]
        self.root=address[1]
        self.size=len(address)

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

    def Postorder(self):
        result=[]
        if self.root==None:
            return None
        def traverse(n):
            if n:
                traverse(n.left)
                traverse(n.right)
                result.append(n.data)
        traverse(self.root)
        print(result)

    def Inorder(self):
        result=[]
        if self.root==None:
            return None
        def traverse(n):
            if n:
                traverse(n.left)
                result.append(n.data)
                traverse(n.right)
        traverse(self.root)
        print(result)

myobj=BinaryTree()
myobj.BuildTree([0,1,2,3,4,5,6,7])


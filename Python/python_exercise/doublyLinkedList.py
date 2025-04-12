class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
class DLL:
    def __init__(self):
        self.head=Node()
        self.last=None
    def insert_data(self,data):
        if self.head.data==None:
            self.head.data=data
            self.Last=self.head
        else:
            new_node=Node(data)
            self.Last.right=new_node
            new_node.left=self.Last
            self.Last=new_node
    def traverse(self):
        if self.head==None:
            return None
        else:
            n=self.head
            while n:
                print(n.data)
                n=n.right 
    def swap(self,a1,a2):
        if a2.right==None:
            a1.left.right=a2
            t1=a1.left
            t2=a2.right
            a1.left=a2
            a2.right=a1
            a1.right=t2
            a2.left=t1
        elif a1.left==None:
            a2.right.left=a1
            t1=a1.left
            t2=a2.right
            a1.left=a2
            a2.right=a1
            a1.right=t2
            a2.left=t1
        else:    
            a1.left.right,a2.right.left=a2.right.left,a1.left.right
            t1=a1.left
            t2=a2.right
            a1.left=a2
            a2.right=a1
            a1.right=t2
            a2.left=t1
    def reverse(self,i1,i2):
        n=self.head
        m=self.head
        address=[]
        for _ in range(i2):
            m=m.right
        stop=m.right
        for _ in range(i1):
            n=n.right
        temp=n
        while temp!=m.right:
            address.append(temp)
            temp=temp.right    
        for i in range(1,i2-i1+1):
            while n.right!=stop:
                self.swap(n,n.right)
            stop=n
            n=address[i]
            if i1==0:
                self.head=n

myobj=DLL()
myobj.insert_data(1)
myobj.insert_data(2)
myobj.insert_data(3)
myobj.insert_data(4)
myobj.insert_data(5)
myobj.insert_data(6)
myobj.reverse(0,5)
myobj.traverse()

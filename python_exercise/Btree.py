class Node:
    def __init__(self,data=None):
        self.data=data
        self.parent=None
        self.lc=None
        self.rc=None
class Binary_tree:
    def __init__(self):
        self.root=Node()
        self.myqueue=[]
    def add_node(self,data):
        if self.root.data==None:
            self.root.data=data
        elif len(self.myqueue)==0:
            self.myqueue.append(self.root)
        else:
            new_node=Node(data)
            if self.myqueue[0].lc:
                self.myqueue[0].rc=new_node 
                self.myqueue.pop(0)
                print('1',new_node.data)
            else:
                self.myqueue[0].lc=new_node
                print('2',new_node.data)
            new_node.parent=self.myqueue[0]
            self.myqueue.append(new_node)    
    def traverse(self,address):
        if self.root==None:
            print("tree is empty")
            return
        elif address:
            print(address.data)
            self.traverse(address.lc)
        if address:
            self.traverse(address.rc)
        
myobj=Binary_tree()
myobj.add_node(21)  
myobj.add_node(10)
myobj.add_node(30)
myobj.add_node(5)
myobj.add_node(12)
myobj.add_node(25)
myobj.add_node(100)
myobj.add_node(3)
myobj.add_node(7)      
myobj.traverse(myobj.root)     
                
            
        
                           
                        


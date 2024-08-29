class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LL:
    def __init__(self):
        self.head=Node(None)
    def push(self,data):
        if self.head.data==None:
            self.head.data=data   
        else:
            new_Node=Node()
            while      
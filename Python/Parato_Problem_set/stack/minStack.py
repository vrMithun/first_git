class Node():
    def __init__(self,data=None):
        self.data=data
        self.ref=None
        self.min=data
class MinStack(object):
    def __init__(self):
        self.head=None
        return None    
    def push(self, data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        n=self.head
        if self.head.ref:
            if n.data<n.ref.min:
                self.head.min=self.head.data
            else:
                self.head.min=n.ref.min    
        return None
    def pop(self):
        if self.head==None:
            return None    
        n=self.head
        self.head=self.head.ref  
        pop=n.data  
        del n
        return pop
    def top(self):
        return self.head.data
    def getMin(self):
        if self.head==None:
            return None
        else:    
            return self.head.min  


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
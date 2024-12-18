class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
        self.height=1
class avl:
    def getheight(self,root):
        if not root:
            return 0
        return root.height
    def balance(self,root):
        return root.left.height-root.right.height
    
    def rightrotate(self,root):
        x=root.left
        y=x.right
        root.left=y
        x.right=root
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x
    
    def leftrotate(self,root):
        x=root.right
        y=x.left
        root.right=y
        x.left=root
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x
        
    def insert(self,root,data):
        if not root:
            return node(data)
        elif root.data<=data:
            root.right=self.insert(root.right,data)
        else:
            root.left=self.insert(root.left,data)
        root.height=max(self.getheight(root.left),self.getheight(root.right))+1

        balance=self.balance(root) 

        if balance>1 and data<root.left.data:
            return self.rightrotate(root)       
        elif balance<1 and data>root.right.data:
            return self.leftrotate(root)
        elif balance >1 and data>root.left.data:
            root.left=root.leftrotate(root.left)
            return self.rightrotate(root)
        elif balance<1 and data<root.right.data:
            root.right=root.rightrotate(root.right)
            return self.leftrotate(root)
        return root
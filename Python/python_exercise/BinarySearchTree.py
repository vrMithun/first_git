class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None
        
    def BuildTree(self, arr):
        for i in range(len(arr)):
            n = self.root
            if self.root == None:  # Set the root for the first element
                self.root = Node(arr[i])
                continue  # Skip further logic for the root

            while n:
                if arr[i] > n.data:  # Go to the right subtree
                    if n.right == None:
                        newNode = Node(arr[i])
                        n.right = newNode 
                        newNode.parent = n
                        break
                    else:
                        n = n.right
                else:  # Go to the left subtree
                    if n.left == None:
                        newNode = Node(arr[i])
                        n.left = newNode
                        newNode.parent = n 
                        break
                    else:
                        n = n.left 

    def preorder(self):
        if self.root == None:
            return None
        else:
            n = self.root
            def traverse(n):
                if n == None:
                    return
                else:
                    print(n.data)
                    traverse(n.left)
                    traverse(n.right)
            traverse(n)

# Example usage:
myobj = BST()
myobj.BuildTree([10, 9, 4, 6, 89, 42, 25, 32])
myobj.preorder()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    # Get the height of the node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Get the balance factor of the node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right rotate subtree rooted with y
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        
        # Return new root
        return x

    # Left rotate subtree rooted with x
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        
        # Return new root
        return y

    # Insert a node into the AVL tree
    def insert(self, root, key):
        # Perform normal BST insertion
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        # Update height of this ancestor node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        
        # Get the balance factor of this ancestor node to check whether it became unbalanced
        balance = self.get_balance(root)
        
        # Left Left Case (LL)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # Right Right Case (RR)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        # Left Right Case (LR)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case (RL)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        # Return the root (unchanged) pointer
        return root

    # Function to do an in-order traversal of the tree
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.key, end=" ")
        self.in_order(root.right)

# Driver code to test the AVL tree
avl = AVLTree()
root = None

# Insert nodes into the AVL tree
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl.insert(root, key)

# In-order traversal to print the AVL tree
print("In-order traversal of the AVL tree is:")
avl.in_order(root)

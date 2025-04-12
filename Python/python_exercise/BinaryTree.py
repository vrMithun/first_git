class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    def rootNode(self):
        return self.root.data if self.root else None
    def preorder_traversal(self):
        result=[]
        def traverse(node):
            if node:
                result.append(node.data)
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        return result
    def postorder_traversal(self):
        result=[]
        def traverse(node):
            if node:
                 traverse(node.left)
                 traverse(node.right)
                 result.append(node.data)
        traverse(self.root)
        return result
    def inorder_traversal(self):
        result = []
        def traverse(node):
            if node:
                traverse(node.left)  # Visit left child
                result.append(node.data)  # Visit current node
                traverse(node.right)  # Visit right child
        traverse(self.root)
        return result
    
    def buildTree(self, eltlist):
        nodeList = [None]  # Placeholder to align indices with 1-based indexing
        for i in range(1, len(eltlist)):
            if eltlist[i] != -1:
                tempnode = Node(eltlist[i])
                nodeList.append(tempnode)
                
                if i != 1:
                    tempnode.parent = nodeList[i // 2]
                    if i % 2 == 0:
                        nodeList[i // 2].left = tempnode
                    else:
                        nodeList[i // 2].right = tempnode
            else:
                nodeList.append(None)
            
        self.root = nodeList[1]  # Set the root to the first node
        self.sz = len(nodeList)
b = BinaryTree()
b.buildTree([0,1, 2, 3, 4, 5, 6, 7])  # 0 is a placeholder to align indexing
print('Preorder Traversal :',end=" ")
print(b.preorder_traversal(),'\n')
print('Postorder Traversal :',end=" ")
print(b.postorder_traversal(),'\n')
print('Inorder Traversal :',end=" ")
print(b.inorder_traversal(),'\n')

'''Key Parts of the Code:
Class Node:

This class represents a node in the binary tree, holding a value (data), a reference to its parent, and two children (left and right).
The parent attribute allows the node to know its parent, which is useful in some tree algorithms.
buildTree Method:

This method builds the tree using a list (eltlist).
The list represents the tree nodes in level order (starting from index 1 for easy 1-based indexing).
The nodeList is initialized with a placeholder None at index 0 to keep alignment with 1-based indexing.
Why Use a List?
The list (eltlist) helps in systematically building the tree, leveraging properties of binary trees:

Parent-Child Relationship in Binary Trees:
For a node at index i in a list:
The left child is at index 2 * i
The right child is at index 2 * i + 1
The parent is at index i // 2
This mathematical relationship simplifies finding the parent or child nodes when constructing a binary tree.
Explanation of buildTree:
Index Alignment:

nodeList = [None]: This initializes the list with a dummy value so that indexing can start from 1 instead of 0, making it easier to calculate the parent-child relationship using the formula mentioned above.
Loop Through eltlist:

The method iterates through eltlist, which contains the node values in level order (starting with index 1).
If the element is not -1 (used as a placeholder for None in this case), a new node is created (tempnode = Node(eltlist[i])).
The parent is found using the index relation (tempnode.parent = nodeList[i // 2]).
The node is added to its parent's left or right child based on whether the index i is even or odd.
Tree Construction:

The tree is built level by level, as the list eltlist is traversed.
The resulting tree structure is stored in the form of connected nodes.
Traversal Methods:
Preorder, Inorder, Postorder Traversals: These methods perform depth-first traversals of the tree:
Preorder: Visit the node first, then its left subtree, followed by its right subtree.
Inorder: Visit the left subtree, then the node, and finally the right subtree.
Postorder: Visit the left subtree, the right subtree, and then the node.
Concept Behind It:
The list allows easy construction of the tree using simple arithmetic on the indices to determine relationships between nodes. This is particularly useful when you want to build a binary tree from a flat structure like a level-order list or when mimicking the structure of binary heaps.

The nodeList ensures the entire tree can be built in a predictable and structured way, without needing complex recursive logic during the construction phase.'''
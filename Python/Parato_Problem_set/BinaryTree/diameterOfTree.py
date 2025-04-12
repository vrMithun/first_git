class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def BuildTree(self, lst):
        address = [None]
        for i in range(1, len(lst)):
            if lst[i] != -1:
                temp = Node(lst[i])
                address.append(temp)
                if i != 1:
                    temp.parent = address[i // 2]  # set parent to the correct node
                    if i % 2 == 0:  # even index, set as left child
                        address[i // 2].left = temp
                    else:  # odd index, set as right child
                        address[i // 2].right = temp
        self.root = address[1]  # root is always at index 1
        self.size = len(address)

    def Preorder(self):
        result = []
        if self.root == None:
            return None
        def traverse(n):
            if n:
                result.append(n.data)
                traverse(n.left)
                traverse(n.right)
        traverse(self.root)
        return result

    def Postorder(self):
        result = []
        if self.root == None:
            return None
        def traverse(n):
            if n:
                traverse(n.left)
                traverse(n.right)
                result.append(n.data)
        traverse(self.root)
        return result

    def Inorder(self):
        result = []
        if self.root == None:
            return None
        def traverse(n):
            if n:
                traverse(n.left)
                result.append(n.data)
                traverse(n.right)
        traverse(self.root)
        return result

    def diameter(self):
        def diameterOfBinaryTree(root):
            # Base case: if the node is None, return height and diameter as 0
            if root is None:
                return 0, 0
            
            # Recursively calculate the height and diameter of left and right subtrees
            left_height, left_diameter = diameterOfBinaryTree(root.left)
            right_height, right_diameter = diameterOfBinaryTree(root.right)
            
            # The height of the current node is 1 + the maximum height of the left or right subtree
            height = 1 + max(left_height, right_height)
            
            # The diameter is the maximum of the current diameter, the left subtree diameter,
            # and the right subtree diameter. Also, check the sum of left and right heights.
            diameter = max(left_diameter, right_diameter, left_height + right_height)
            
            return height, diameter
        
        _, diameter = diameterOfBinaryTree(self.root)
        return diameter


# Test cases for BinaryTree class
test_cases = [
    ([0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 3, 7, 6, 2, 5, 4], [3, 1, 7, 0, 6, 5, 4, 2], 5),  # Test case 1
    ([1, 2, 3, -1, 4, 5], [1, 2, 4, 5, 3], [2, 4, 1, 5, 3], 3),                       # Test case 2
    ([10, 20, 30, -1, -1, 40, 50], [10, 20, 40, 30, 50], [20, 10, 40, 30, 50], 3),    # Test case 3
    ([1, 2, 3, -1, -1, -1], [1, 2, 3], [1, 2, 3], 2),                                  # Test case 4
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 4)                           # Test case 5
]

# Running the test cases
for i, (arr, preorder, inorder, expected_diameter) in enumerate(test_cases, 1):
    myobj = BinaryTree()
    myobj.BuildTree(arr)
    diameter = myobj.diameter()
    print(f"Test case {i}:")
    print(f"  Input: {arr}")
    print(f"  Preorder: {myobj.Preorder()} -> Expected: {preorder}")
    print(f"  Inorder: {myobj.Inorder()} -> Expected: {inorder}")
    print(f"  Diameter: {diameter} -> Expected: {expected_diameter}")
    print("-" * 50)

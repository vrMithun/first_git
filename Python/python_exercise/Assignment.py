class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def buildBST(preorder):
    if not preorder:
        return None

    def insert(root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
        return root

    root = None
    for key in preorder:
        root = insert(root, key)
    return root

def levelOrderTraversal(root):
    if root is None:
        return []
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.extend(current_level)
    
    return result

def constructBSTAndGetLevelOrder(preorder):
    root = buildBST(preorder)
    return levelOrderTraversal(root)


preorder = [10, 5, 1, 7, 40, 50]
level_order = constructBSTAndGetLevelOrder(preorder)
print(level_order) 

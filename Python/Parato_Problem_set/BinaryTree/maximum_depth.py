class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0  
        
        queue = [root]
        depth = 0
        
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth

# Test cases to validate the maxDepth function

# 1. Empty Tree
# Input: None
# Output: 0

# 2. Single Node Tree
# Input: [1]
# Output: 1

# 3. Balanced Tree
# Input:      1
#           /   \
#          2     3
#         / \   / \
#        4   5 6   7
# Output: 3

# 4. Left-Skewed Tree
# Input:      1
#           /
#          2
#         /
#        3
# Output: 3

# 5. Right-Skewed Tree
# Input:  1
#           \
#            2
#             \
#              3
# Output: 3

# 6. Tree with Mixed Missing Children
# Input:      1
#           /   \
#          2     3
#         /       \
#        4         5
# Output: 3

# 7. Large Tree
# Input: A linear tree (e.g., 1 -> 2 -> 3 -> ... -> n)
# Output: n (where n is the depth of the tree)

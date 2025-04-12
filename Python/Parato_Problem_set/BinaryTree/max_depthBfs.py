# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root==None:
            return 0
        stack=[root]
        depth=0
        while stack:
            depth+=1
            for _ in range(len(stack)):
                node=stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return depth                               

# Test cases to validate the solution

# 1. Empty tree (edge case: root is None)
# Input: None
# Output: 0

# 2. Single node tree (edge case: depth is 1)
# Input:  [1]
# Output: 1

# 3. Tree with only left subtree (unbalanced)
# Input:      1
#            /
#           2
#          /
#         3
# Output: 3

# 4. Tree with only right subtree (unbalanced)
# Input:  1
#           \
#            2
#             \
#              3
# Output: 3

# 5. Full binary tree
# Input:      1
#           /   \
#          2     3
#         / \   / \
#        4   5 6   7
# Output: 3

# 6. Tree with mixed missing children
# Input:      1
#           /   \
#          2     3
#         /       \
#        4         5
# Output: 3

# 7. Large tree (test for performance)
# Input: A binary tree with depth > 1000
# Output: Correct depth (e.g., 1001 for a linear tree with 1001 nodes)

# 8. Tree with duplicate values (validate depth calculation, not node values)
# Input:      1
#           /   \
#          1     1
#         / \   / \
#        1   1 1   1
# Output: 3


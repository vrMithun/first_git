# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root:
            self.invertTree(root.right)
            self.invertTree(root.left)
            temp=root.right
            root.right=root.left
            root.left=temp   
        return root

 # Test cases to validate the solution

# 1. Single node tree (edge case: no children to swap)
# Input:  [1]
# Output: [1]

# 2. Empty tree (edge case: root is None)
# Input:  []
# Output: []

# 3. Tree with only left subtree
# Input:      1
#            /
#           2
# Output:     1
#              \
#               2

# 4. Tree with only right subtree
# Input:  1
#           \
#            2
# Output:    1
#           /
#          2

# 5. Full binary tree (common case)
# Input:      1
#           /   \
#          2     3
#         / \   / \
#        4   5 6   7
# Output:      1
#           /   \
#          3     2
#         / \   / \
#        7   6 5   4

# 6. Unbalanced tree with deeper left subtree
# Input:      1
#           /
#          2
#         /
#        3
# Output:      1
#               \
#                2
#                 \
#                  3

# 7. Unbalanced tree with deeper right subtree
# Input:  1
#           \
#            2
#             \
#              3
# Output:      1
#           /
#          2
#         /
#        3

# 8. Tree with a mix of missing left and right children
# Input:      1
#           /   \
#          2     3
#         /       \
#        4         5
# Output:      1
#           /   \
#          3     2
#         /       \
#        5         4

# 9. Large tree (test for performance and stack overflow)
# Input: A large binary tree with depth > 1000
# Output: A correctly inverted large binary tree

        
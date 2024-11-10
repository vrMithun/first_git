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
        
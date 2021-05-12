# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        level = 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        level += max(left, right)
        return level
        
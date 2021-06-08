# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def search(node):
            if not node:
                return 0
            value = 0
            if low <= node.val and node.val <= high:
                value += node.val
            value += search(node.left)
            value += search(node.right)
            return value
        return search(root)
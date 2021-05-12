# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirror(n1, n2):
            if (n1 == None and n2 == None):
                return True
            elif (n1 == None or n2 == None):
                return False
            return (n1.val == n2.val) and mirror(n1.left, n2.right) and mirror(n1.right, n2.left)
        return mirror(root, root)
            
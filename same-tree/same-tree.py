# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         def sameChildren(left, right):
#             if left.left.val == right.left.val and left.right.val == right.right.val:
#                 return True
#             else:
#                 return False
#         def search(left, right):
#             if left == None and right == None:
#                 return True
        
#             if left.left == None and left.right == None and right.left == None and right.right == None:
#                 if left.val == right.val:
#                     return True
#                 else:
#                     return False
            
#             if left.val == right.val:
#                 # continue search
#                 search(left.left, right.left)
#                 search(left.right, right.right)
#             else:
#                 return False
            
#             return True
#         return search(p, q)
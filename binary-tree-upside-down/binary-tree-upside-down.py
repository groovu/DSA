# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        # read in the tree, which order? in order, left root right
        # read out into new tree, left = root, root = right, right = left.
        
        # [1, 2, 3]
        # [2, 1, 3] # wrong root should be right.
        def dfs(node):
            if node is None:
                return None
            if not node.left:
                return node
            
            
            newRoot = dfs(node.left)
            node.left.left = node.right
            node.left.right = node
            node.left = None
            node.right = None
            
            
            return newRoot
            
            
        
        return dfs(root)
        
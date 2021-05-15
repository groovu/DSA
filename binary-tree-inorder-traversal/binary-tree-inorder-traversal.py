# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #in order node, left, right?
        
        stack = []
        result = []
        
        node = root
        while node or len(stack) != 0:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def explore(node, target):
            result = []
            while node.val != target.val:
                result.append(node)
                if node.val > target.val:
                    node = node.left
                else:
                    node = node.right
            result.append(target)
            return result
        p_ancestor = explore(root, p)
        q_ancestor = explore(root, q)
        
        print(p_ancestor)
        print(q_ancestor)
        
        if len(p_ancestor) < len(q_ancestor):
            for i in p_ancestor[::-1]:
                if i in q_ancestor:
                    return i
        else:
            for i in q_ancestor[::-1]:
                if i in p_ancestor:
                    return i
        
            
            
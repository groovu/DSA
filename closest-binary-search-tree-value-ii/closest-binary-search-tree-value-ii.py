# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        values = []
        def search(node):
            if node:
                values.append(node.val)
                # lol why doesn't += work?
                search(node.left)
                search(node.right)

        
        search(root)
        values.sort(key = lambda x: abs(x - target))
        
        return values[:k]
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
#         def search(node, target):
#             if node == None:
#                 return
#             if target == node.val:
#                 return node.val
#             search(node.left, target)
#             search(node.right, target)
        
#         rounded = round(target)
        
#         return search(root, rounded)
        closest = root.val
        node = root
        while node:
            node_info = [node.val, abs(node.val - target)]
            closest_info = [closest, abs(closest - target)]
            if node_info[1] < closest_info[1]:
                closest = node_info[0]
            else:
                closest = closest_info[0]
            
            if node.val > target:
                node = node.left
            else:
                node = node.right
        
        return closest
        
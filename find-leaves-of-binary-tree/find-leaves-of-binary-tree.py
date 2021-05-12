# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                level = max(left, right) + 1
                dic[level] += [node.val]
                return level
            else:
                return 0
        dic = defaultdict(list)
        dfs(root)
        return list(dic.values())
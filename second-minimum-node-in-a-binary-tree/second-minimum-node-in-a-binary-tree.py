# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # assuming a binary tree is sorted, the left most node should be the smallest value.
        # search nodes
        # left and right
        # should return min value of each side?
        # min(left, right?)
        # no, wouldn't work since min and 2nd min could both be on one side
        # somehow search and return two values?

        # ok, based on the prompt, the root node is always the smallest.ArithmeticError
        # so search for stuff that is smallest < target <  last smallest?
        
        self.result = math.inf
        min_val = root.val
        
        def dfs(node):
            if node:
                if min_val < node.val < self.result:
                    self.result = node.val
                else:
                    dfs(node.left)
                    dfs(node.right)
        
        dfs(root)
        if self.result == math.inf:
            return -1
        else:
            return self.result
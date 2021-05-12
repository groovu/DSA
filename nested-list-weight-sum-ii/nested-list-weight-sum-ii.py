# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # traverse through each node
        # record depth and node val.
        # at then we have the max depth
        # and can calculate weight of each node
        # sum for answer.
        
        dic = defaultdict(list)
        
        def dfs(nodes, level):
            for node in nodes:
                if node.isInteger():
                    dic[level] += [node.getInteger()]
                else:
                    dfs(node.getList(), level + 1)
        
        dfs(nestedList, 1)
        if not dic:
            return 0
        max_depth = max(dic.keys())
        total = 0
        for k, v in dic.items():
            weight = max_depth - (k) + 1
            for value in v:
                total += weight * value
        
        return(total)
        
        
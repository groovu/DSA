class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        delta = [target - i for i in nums]
        for i in range(len(delta)):
            if delta[i] in nums:
                if i != nums.index(delta[i]):
                    return [i, nums.index(delta[i])]
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in res.keys():
                return [res.get(complement), i]
            res[nums[i]] = i
        return []
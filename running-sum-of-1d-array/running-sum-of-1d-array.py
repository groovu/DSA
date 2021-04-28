class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            if i == 0:
                lst.append(nums[0])
            else:
                lst.append(lst[i-1] + nums[i])
        
        return lst
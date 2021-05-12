class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        print(nums)
        print(accumulate(nums))
        for i in accumulate(nums):
            print(i)
        
        return max(1, -min(accumulate(nums)) + 1)
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        less_k = -1
        i = 0
        j = len(nums) - 1
        while i < j:
            total = nums[i] + nums[j]
            if total < k:
                less_k = max(less_k, nums[i] + nums[j])
                i += 1
            else:
                j -= 1
        return less_k
            
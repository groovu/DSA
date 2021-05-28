class Solution:
    def search(self, nums: List[int], target: int) -> int:
        max_val = max(nums)
        max_idx = nums.index(max_val)
        start = nums[0]
        end = nums[-1]
        
        
        def binSearch(target, arr):
            mid = len(arr)//2
            
        
        # if target between nums[0] and max_val
        # search nums[0:max_idx]
        # if target between nums[max_idx + 1] and end
        # search nums[max_idx+1:]
        # binary search on whichever path.
        # if nums[0] <= target <= nums[max_idx]:
        #     print("left")
        # elif nums[max_idx+1] <= target <= nums[-1]:
        #     print("right")
        
        if target in nums:
            return nums.index(target)
        else:
            return -1
        #return nums.index(target) # this works, but is O(n)
        # improve this to O(log(n)) using binsearch
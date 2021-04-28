class Solution:
    def search2(self, nums: List[int], target: int) -> int:
        # split the list into two, check last index of left, check last index of right
        # if != target, repeat search.
        # could be improved since the list is sorted, only need to check one of the two.
        size = len(nums)
        left = nums[:size//2]
        right = nums[size//2:]
        print(type(nums))
        print(type(left))
        if len(left) == 0 or len(right) == 0:
            return -1
        left_val = nums[size//2]
        right_val = nums[size//2 + 1]
        if left_val == target:
            return len(left)
        elif right_val == target:
            return len(left) + 1
        else:
            print(type(nums))
            print(type(left))
            search(self, left, target)
            search(self, right, target)
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        # indices
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = left + (right - left) // 2
            # calculates middle
            # [0, 1, 2, 3, 4, 5]
            # l = 0, r = 5
            # m = 0 + (5 - 0) // 2 = 0 + 2 = 2
            # hard to wrap head around, but this prevents us from skipping when we split.
            
            if nums[middle] == target:
                return middle
            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1
    
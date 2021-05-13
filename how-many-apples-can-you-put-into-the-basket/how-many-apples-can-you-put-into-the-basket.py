class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            if sum > 5000:
                return i
        return len(arr)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [i ** 2 for i in nums]
        arr.sort()
        return arr
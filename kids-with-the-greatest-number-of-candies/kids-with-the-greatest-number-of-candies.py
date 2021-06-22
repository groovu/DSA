class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        richest = max(candies)
        for i in range(len(candies)):
            candies[i] += extraCandies
        result = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] >= richest:
                result[i] = True
        return result
        
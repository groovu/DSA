class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         min_val = min(prices)
#         max_val = max(prices)
        
#         min_indices = [i for i, x in enumerate(prices) if x == min_val]
#         max_indices = [i for i, x in enumerate(prices) if x == max_val]
        
#         first_min_index = min_indices[0]
        
#         for i in max_indices:
#             if i > first_min_index:
#                 return prices[i] - prices[first_min_index]
    # above doesn't work right now because sometimes the max val comes before the min
    # problem with above is: you have to keep track of which min or max is the best
    # while following the constraint of them being sequential.
        maxCur = 0
        maxSoFar = 0

        for i in range(1, len(prices)):
            delta = prices[i] - prices[i-1]
            maxCur += delta
            maxCur = max(0, maxCur)
            maxSoFar = max(maxCur, maxSoFar)

        return maxSoFar
    # this is more elegant, and runs in O(n) time
    # space complexity O(1)?
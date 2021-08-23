class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        cur_sum = 0
        
        for num in nums:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         max_sum = -float("inf")
#         cur_sum = 0
        
#         for num in nums:
#             cur_sum = max(cur_sum + num, num)
#             max_sum = max(max_sum, cur_sum)
        
#         return max_sum

# # imo this works, but two for loops is too slow.
# # class Solution:
# #     def maxSubArray(self, nums: List[int]) -> int:
# #         # Since I'm only keeping track of the largest sum
# #         # I can just iterate through each index.
# #         # and at each index, iterate to the end of the array.
# #         # keep track of the max value so far, and return that value.
# #         # Would this be more complicated if I also had to return the array that gave the max sum?
        
# #         maxSum = -math.inf
# #         length = len(nums)
# #         for i in range(length): # iterate through each index
# #             # maxSoFar = -math.inf # value to keep track of max of sub array iteration.
# #             subSum = 0 # initialize start value for sub array
# #             for j in range(i, length): # iterate through each index starting at i.
# #                 subSum += nums[j] 
# #                 maxSum = max(maxSum, subSum)
# #                 # if maxSoFar < subSum: # keeping track of maxSoFar in subarry
# #                 #     maxSoFar = subSum
# #             # maxSum = max(maxSum, maxSoFar)
# #             # if maxSum < maxSoFar: #if maxSoFar is breater than the max seen in previous iterations
# #             #     maxSum = maxSoFar # update maxSum
        
# #         return maxSum
        
# #         #solution is too slow. timed out.
# #         # small things like if and max are costly when your input is huge.
# #         # after getting your scratch work done, remove the redundant work.

#         #max_sum = -math.inf
# #         current_sum = 0
        
# #         for num in nums:
# #             current_sum = max(current_sum+num,num)
# #             max_sum = max(current_sum,max_sum)
        
# #         return max_sum
        
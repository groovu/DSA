class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # row of n houses.
        # each house has a cost for r,b,g
        # paint the houses such that
        # no adjacent house has the same color
        # and the total cost is minimized
        
        # try something greedy?
        # first house, choose min
        # second house, 2 choices, choose min
        # third hosue, 2 choices, choose min
        # repeat until done.
        
#         total = 0
        
#         def greedyMin(i, prev):
#             house = costs[i]
#             if i == len(costs) - 1:
#                 return min(house), house.index(min(house))
#             house[prev] = math.inf
#             return min(house), house.index(min(house))
        
#         prev = -1
#         for i in range(len(costs) - 1, -1, -1):
#             min_house, prev = greedyMin(i, prev)
#             total += min_house
        
#         # working forwards gives wrong result, but working backwards is ok?
#         return total
        
        if len(costs) == 0:
            return 0
        
        for i in reversed(range(len(costs) - 1)):
            for j in range(3):
                costs[i][j] += min(costs[i+1][(j+1)%3], costs[i+1][(j+2)%3])
        
        return min(costs[0])
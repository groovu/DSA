class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # dfs solution
        @lru_cache(maxsize = None)
        def dfs(x, y):
            #base case
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            else:
                return min(dfs(abs(x-1), abs(y-2)), dfs(abs(x-2), abs(y-1))) + 1
        
        return dfs(abs(x), abs(y))

        
#         moves = [(2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1,-2)]
        
#         def bfs(target_x, target_y):
#             visited = set()
#             q = deque([(0,0)])
#             steps = 0
            
#             while q:
#                 for i in range(len(q)):
#                     cur_x, cur_y = q.popleft()
#                     if cur_x < 0 or cur_y < 0:
#                         break
#                     if (cur_x, cur_y) == (target_x, target_y):
#                         return steps

#                     for x, y in moves:
#                         next_x = cur_x + x
#                         next_y = cur_y + y
#                         if (next_x, next_y) not in visited:
#                             visited.add((next_x, next_y))
#                             q.append((next_x, next_y))

#                 steps += 1
        
#         return bfs(abs(x), abs(y))
    
    
#         # bfs setup
#         # init visited
#         # init queue
#         # set up tracker (could be steps, or moves, w/e)
        
#         # while q is not empty:
#             #iterate through q
#             #pop front item (FIFO)
#             #if next item is target, return
#             #else continue search
#             #   build next items to search
#             #   add items to visited and q
#             #update tracker
            
#         #return only happens when target is possible
#         #add error / bound checks depending on the question.
#         # in this case, it's an infinite grid.
        
#         # improvements?
#         # could make BFS only build items that are in direction of target.
        
#         # ex: target is (pos, pos)
#         # so only add items that have pos pos 
#         # but this could be a problem, like in chess, to get to (1,1)
#         # you need to go negative before going positive. 
#         # so how would you improve this for chess?
        
#         # one strat to cut the work in half is to use the property
#         # that it takes the same amount of moves to get to (x, y) as (-x, y)
#         # could you cut in half again in a way that getting to (x,y) is same as (-x, -y); probably!
        
        
        
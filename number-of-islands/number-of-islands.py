class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate over each index
        # if we find land, increase island count by 1.
        # search all 4 directions to find contigious land mass
        # flip to 0 to indicate we've looked at it.
        # when everything returns 0
        # continue with search.
        max_y = len(grid) - 1
        max_x = len(grid[0]) - 1

        def bfs(y, x):
            print(y, x)
            if grid[y][x] == "0":
                return
            if grid[y][x] == "1":
                grid[y][x] = "0"
                up_y, up_x = min(y+1, max_y), x
                d_y, d_x = max(y-1, 0), x
                l_y, l_x = y, max(x-1, 0)
                r_y, r_x = y, min(x+1, max_x)
                bfs(up_y, up_x)
                bfs(d_y, d_x)
                bfs(l_y, l_x)
                bfs(r_y, r_x)


        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)
        return islands

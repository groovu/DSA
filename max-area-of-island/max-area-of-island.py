class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # base case: grid[x][y] == 1, then area size 1.
        # search up, down, left, right.  add to base
        # edge cases:
        # out of bounds
        #
        # we can mutate the map to keep track of what we've seen
        self.map = grid
        maxArea = 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        for r in range(self.rows):
            for c in range(self.cols):
                if self.map[r][c] == 1:
                    maxArea = max(maxArea, self.search(r,c))
        
        return maxArea
    
    def search(self, row, col):
        if (row < 0 or col < 0):
            return 0
        if (row >= self.rows or col >= self.cols):
            return 0
        if self.map[row][col] == 0:
            return 0
        self.map[row][col] = 0
        return 1 + self.search(row, col - 1) + self.search(row, col + 1)+ self.search(row - 1, col)+ self.search(row + 1, col)
        
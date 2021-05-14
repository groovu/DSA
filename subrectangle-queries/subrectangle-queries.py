class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle
        
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # get the dif x, dif y
        # iterate through x rows
        # iterate through y cols
        # update self.matrix[x][y] = newVal
        dif_x = row2 - row1 # num of rows to interate over
        dif_y = col2 - col1

        for r in range(dif_x + 1):
            for c in range(dif_y + 1):
                #print(self.matrix[row1+r][col1+c])
                self.matrix[row1+r][col1+c] = newValue
                #print(self.matrix[row1+r][col1+c])

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]
        
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

# Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

# Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
# 2. getValue(int row, int col)

# Returns the current value of the coordinate (row,col) from the rectangle.

# input matrix of integers
# def update r1, c1, r2, c2, newVal

# assumptions:
# never empty or negative
# all values positve
# invalid coordinates?  always valid.

# 1 1 1
# 1 1 1
# 1 1 1 

#update(0,0, 1, 1, 5)
# 5 5 1
# 5 5 1
# 1 1 1

# approaches































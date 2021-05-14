# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dims = binaryMatrix.dimensions()
        row, col = dims[0], dims[1]
        
        low_col = col
        
        for i in range(row):
            print("i = ", i)
            head = 0
            tail = col - 1
            
            while head < tail:
                print(head, tail)
                mid = (head + tail) // 2
                val = binaryMatrix.get(i, mid)
                print(val)

                if val == 0:
                    head = mid + 1
                else:
                    tail = mid
        
            if binaryMatrix.get(i, tail) == 1:
                low_col = min(low_col, head)
                
        
        return -1 if low_col == col else low_col
    
    
#         for i in range(row):
#             mid = col // 2
#             while True:
#                 val = binaryMatrx.get(i, mid)
#                 if val == 1: # look left
#                     if low_col > mid:
#                         low_col = mid
#                     mid = mid // 2
#                     if mid == 
#                 if val == 0:
#                     mid = mid + (mid // 2)
#         print(dims)
        
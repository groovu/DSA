class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = sqrt(num)
        
        if x % 1 != 0:
            return False
        return True
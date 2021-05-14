class Solution:
    def reverse(self, x: int) -> int:
        lower = -2 ** 31
        upper = 2 ** 31 - 1
        
        is_negative = x < 0

        result = 0
        
        x = abs(x)
        
        while x != 0:
            last = x % 10
            result = result * 10 + last
            x = x // 10
        
        if lower > result or upper < result:
            print(lower)
            print(result)
            print(upper)
            return 0
        
        if is_negative:
            return -result
        else:
            return result
        
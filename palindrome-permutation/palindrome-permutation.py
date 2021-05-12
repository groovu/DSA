class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd = set()
        for c in s:
            if c not in odd:
                odd.add(c)
            else:
                odd.remove(c)
        
        if len(odd) == 0 or len(odd) == 1:
            return True
        else:
            return False
        
class Solution:
    def validPalindrome(self, s: str) -> bool:
        front = 0
        end = len(s) - 1
        
        deleted = 0
        while front < end:
            if s[front] != s[end]:
                skip_front = s[front:end]
                skip_end = s[front+1 : end+1]
                if skip_front == skip_front[::-1] or skip_end == skip_end[::-1]:
                    return True
                else:
                    return False
            front += 1
            end -= 1
        
        return True
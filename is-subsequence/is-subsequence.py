class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx = 0
        
        s_len = len(s)
        t_len = len(t)
        
        while s_idx < s_len and t_idx < t_len:
            if s[s_idx] == t[t_idx]:
                s_idx +=1
            t_idx += 1
            
        if s_idx == s_len:
            return True
        else:
            return False
        
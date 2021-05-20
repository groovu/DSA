class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        set_s = {}
        set_t = {}
        
        for i in range(len(s)):
            if s[i] in set_s and t[i] != set_s[s[i]]:
                return False
            if t[i] in set_t and s[i] != set_t[t[i]]:
                return False
            
            set_s[s[i]] = t[i]
            set_t[t[i]] = s[i]
        return True
        
        
#         s_set = set(s)
#         t_set = set(t)
#         s_count = {}
#         t_count = {}
        
#         def counter(x_set, x_count, x_string):
#             for c in x_set:
#                 x_count[c] = x_string.count(c)
                
#         counter(s_set, s_count, s)
#         counter(t_set, t_count, t)
        
#         s_values = list(s_count.values()).sort()
#         t_values = list(t_count.values()).sort()

#         if len(s_set) == len(t_set) and s_values == t_values:
#             return True
#         else:
#             return False
        
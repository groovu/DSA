class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_dict = {}
        
        for c in t:
            if c not in t_dict:
                t_dict[c] = 1
            else:
                t_dict[c] += 1
        
        head = tail = 0
        counter = len(t_dict)
        shortest_so_far = math.inf
        
        result = ""
        
        while tail < len(s):
            char = s[tail]
            if char in t_dict:
                t_dict[char] -= 1
                if t_dict[char] == 0:
                    counter -= 1
            tail += 1
            
            while counter == 0: # found valid substring
                if (tail - head) < shortest_so_far:
                    shortest_so_far = tail - head
                    result = s[head:tail]
                
                h_char = s[head]
                if h_char in t_dict:
                    t_dict[h_char] += 1
                    if t_dict[h_char] > 0:
                        counter += 1
                head += 1
                
        return result
        
            
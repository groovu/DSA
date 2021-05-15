class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs, key = len)
        strs.remove(min_str)

        for i in range(len(min_str)):
            for s in strs:
                if s[i] != min_str[i]:
                    return min_str[0:i]
        
        return min_str
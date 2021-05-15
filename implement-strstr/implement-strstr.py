class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range(len(haystack)):
            if haystack[i] != needle[0]:
                continue
            elif haystack[i:len(needle)+i] == needle:
                return i
        
        return -1
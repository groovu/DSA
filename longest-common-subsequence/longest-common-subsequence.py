class Solution:
    @lru_cache(maxsize=None)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #base case
        str1 = text1
        str2 = text2
        if len(str1) == 0 and len(str2) == 0:
            return 0
        # case 1
        # both end with same char, drop char on both strings
        # recursive call with new strings
        # result = 1 + recursive call.
        
        # case 2
        # both end with diff char
        # two recursive calls
        # lcs(str1, str2 - last char)
        # lcs(str1 - last char, str 2)
        # result = max of two.
        
        if len(str1) == 0 or len(str2) == 0:
            return 0
        
        if str1[-1] == str2[-1]:
            result = 1 + self.longestCommonSubsequence(str1[:-1], str2[:-1])
        else:
            result = max(self.longestCommonSubsequence(str1, str2[:-1]), self.longestCommonSubsequence(str1[:-1], str2))
            
        return result
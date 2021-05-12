class Solution:
    def countLetters(self, S: str) -> int:
        summer = [0] * len(S)
        summer[0] = 1
        for i in range(1,len(S)):
            if S[i-1] == S[i]:
                summer[i] = summer[i - 1] + 1
            else:
                summer[i] = 1
        
        return sum(summer)
            
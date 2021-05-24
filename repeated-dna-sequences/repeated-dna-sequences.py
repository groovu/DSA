class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        result = set()
        
        width = 10
        index = 0
        while index + width <= len(s):
            sub = s[index:index+width]
            if sub in seen:
                result.add(sub)
            else:
                seen.add(sub)
            index += 1
                
        return list(result)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #keeps track of openings.
        dict = {"]":"[", "}":"{", ")":"("}
        for c in s:
            if c in dict.values():
                stack.append(c)
            elif c in dict.keys():
                if stack == []:
                    return False
                popped = stack.pop()
                if dict[c] != popped:
                    return False
            else:
                return False
        
        if stack == []:
            return True
        else:
            return False
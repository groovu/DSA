class Solution:
    def decodeString(self, s: str) -> str:
        # idea: we turn the input into a stack
        # build strings and number of reps using stack.
        # whenever we open a brack, we append the stack and build a new chunk
        # whenver we close a brack, we pop the stock and update the return string.
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curNum = 0
                curString = ''
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + curString * num
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        
        return curString
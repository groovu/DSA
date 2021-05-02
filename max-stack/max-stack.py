class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        #use a stack and add the max functionality.
        self.stack = []
        self.maxSoFar = -math.inf
        self.maxIndices = []
        
        
        
        
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.maxSoFar < x:
            self.maxSoFar = x
            self.maxIndices = [len(self.stack) - 1]
        elif self.maxSoFar == x:
            self.maxIndices.append(len(self.stack) - 1)
            
        

    def pop(self) -> int:
        # situations
        # pop == max and max changes
        #   how do I retrieve the previous max index/indices?
        #   get new maxSoFar
        #   rebuild maxIndices.
        # pop != max
        #   remove top and return.
        # 
        popped = self.stack.pop()
        if popped == self.maxSoFar:
            if len(self.maxIndices) == 1:
                self.rebuildMax()
            else:
                self.maxIndices = self.maxIndices[:-1]
        return popped
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def peekMax(self) -> int:
        if (len(self.maxIndices) == 0):
            return
        return self.stack[self.maxIndices[0]]
        

    def popMax(self) -> int:
        # get max last index.
        # remove max
        # if max chanes, rebuild max details.
        maxIndex = self.maxIndices[-1]
        self.maxIndices = self.maxIndices[:-1]
        maxVal = self.stack[maxIndex]
        newStack = []
        count = 0
        for i in range(len(self.stack)):
            if i == maxIndex:
                continue
            else:
                newStack.append(self.stack[i])
                count += 1
        self.stack = newStack
        
        if len(self.maxIndices) == 0:
            self.rebuildMax()
        
        return maxVal
    
    def rebuildMax(self):
        if (len(self.stack) == 0):
            self.maxSoFar = -math.inf
            return
        newMax = max(self.stack)
        newMaxIndices = []
        index = 0
        for i in self.stack:
            if i == newMax:
                newMaxIndices.append(index)
            index += 1
        self.maxSoFar = newMax
        self.maxIndices = newMaxIndices
        
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


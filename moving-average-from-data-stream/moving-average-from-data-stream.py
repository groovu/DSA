class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = size
        self.values = []
        # since we are only tracking the moving average
        # we can reduce our memory usage by only tracking the window size.
        

    def next(self, val: int) -> float:
        self.values.append(val)
        if (len(self.values) > self.window):
            self.values.pop(0) # get rid of first outside of window
        window_sum = sum(self.values) 
        return window_sum/min(self.window, len(self.values))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
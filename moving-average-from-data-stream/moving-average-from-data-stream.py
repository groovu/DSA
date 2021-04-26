class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = size
        self.values = []
        

    def next(self, val: int) -> float:
        self.values.append(val)
        window_sum = sum(self.values[-self.window:]) # [start:end], negative start means it'll wrap around.
        return window_sum/min(self.window, len(self.values))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
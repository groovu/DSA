class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.values[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in self.values:
            remainder = value - i
            if remainder in self.values:
                if remainder != i or (remainder == i and self.values[remainder] >= 2):
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
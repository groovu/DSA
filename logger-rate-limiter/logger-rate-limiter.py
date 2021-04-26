class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # we could use a dict to keep track of words and the time stamp.
        # new messages we just add to the dict
        # old messages, we check the timestamp
        # if new time valid, update timestamp and return true
        # else return false
        self.msg_dict = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.msg_dict:
            if self.msg_dict[message] + 10 > timestamp:
                return False
            else:
                self.msg_dict[message] = timestamp
                return True
            
        else:
            self.msg_dict[message] = timestamp
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
class Logger:

    def __init__(self):
        self.msg = {}
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg:
             self.msg[message] = timestamp + 10
             print(self.msg)
             return True
        else:
            print(self.msg[message],timestamp)
            if self.msg[message] <= timestamp:
                self.msg[message] = timestamp +10
                return True
            else:
                return False
        print(self.msg)            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
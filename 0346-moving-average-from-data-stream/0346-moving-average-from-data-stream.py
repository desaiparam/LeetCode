class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = []
        self.actualsize = 0

    def next(self, val: int) -> float:
        self.actualsize += 1
        self.window.append(val)
        if self.actualsize <= self.size:
            return sum(self.window)/ self.actualsize
        else:
            return sum(self.window[self.actualsize - self.size:]) / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
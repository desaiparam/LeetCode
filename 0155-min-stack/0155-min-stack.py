class MinStack:

    def __init__(self):
        self.stack = []
        # self.map = {}
        self.min = []

    def push(self, val: int) -> None:
        # if self.min > val:
        #     self.min = val
        # print(self.min)
        # self.map[value] = len(self.stack)
        self.stack.append(val)
        if not self.min or self.min[-1] >= val :
            self.min.append(val)

    def pop(self) -> None:
        # if not in self.map:
        #     self.map.remove()
        #     self
        # print(self)
        val_remo=self.stack.pop()
        if  val_remo == self.min[-1]:
            self.min.pop()  
        # self.min
        # self.stack.pop()
     
        # self.stack.pop(0)

    def top(self) -> int:
        # print(self)
        # self.min = self.stack.pop(0)
        # print(self.min) 
        # print("top",self.stack.pop())
        return self.stack[-1]

    def getMin(self) -> int:
        # print(self.stack)
        # return self.min
        # if self.stack is None:
        #     return -1
        return self.min[-1]
        # self.stack



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
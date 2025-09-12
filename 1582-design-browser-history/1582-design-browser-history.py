class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = []
        self.pos = 0
        self.stack.append(homepage)
        

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.pos+1]
        self.stack.append(url)
        self.pos = len(self.stack) - 1
        print("visit",self.stack,self.pos)

    def back(self, steps: int) -> str:
        self.pos = max(0,self.pos - steps)
        print("back",self.stack,self.pos)
        return self.stack[self.pos]
        

    def forward(self, steps: int) -> str:
        self.pos = min(len(self.stack)-1,self.pos + steps)
        print("forward",self.stack,self.pos)
        return self.stack[self.pos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
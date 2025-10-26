class PhoneDirectory:
            
    def __init__(self, maxNumbers: int):
        self.seen = set()
        self.q = deque()
        for i in range(maxNumbers):
            self.q.append(i)
    def get(self) -> int:
        if not self.q:
            return -1
        curr = self.q.popleft()
        self.seen.add(curr)
        return curr
    
    def check(self, number: int) -> bool:
        if number in self.seen:
            return False
        return True
        

    def release(self, number: int) -> None:
        if number in self.seen:
            self.seen.remove(number)
            self.q.append(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
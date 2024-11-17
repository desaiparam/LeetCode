class RandomizedSet:

    def __init__(self):
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = val
            return True 
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            self.map.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        # print(self.map)
        return random.choice(list(self.map.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
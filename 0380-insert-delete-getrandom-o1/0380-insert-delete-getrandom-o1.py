class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.value = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.value)
            self.value.append(val)
            return True 
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            index = self.map[val]
            l_v = self.value[-1]

            self.value[index] = l_v
            self.map[l_v] = index

            self.value.pop()
            del self.map[val]
            return True
        return False
        

    def getRandom(self) -> int:
        # print(self.map)
        return random.choice(self.value)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
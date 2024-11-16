class TwoSum:

    def __init__(self):
        self.map = {}

    def add(self, number: int) -> None:
        if number in self.map:
            self.map[number] += 1  # Increment the count if number already exists
        else:
            self.map[number] = 1 


    def find(self, value: int) -> bool:
        for i in self.map:
            c = value-i
            if c in self.map and (c!=i or self.map[i] >1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
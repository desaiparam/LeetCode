class MyHashSet:

    def __init__(self):
        self.maping = collections.defaultdict(int)

    def add(self, key: int) -> None:
        self.maping[key] = 1

    def remove(self, key: int) -> None:
        self.maping.pop(key,None)

    def contains(self, key: int) -> bool:
        return self.maping[key] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
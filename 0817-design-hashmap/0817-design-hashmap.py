class MyHashMap:

    def __init__(self):
        self.bucket = [None] * 1000
        
    def hash1(self,key:int):
        return key%1000
    def hash2(self,key:int):
        return key//1000
    def put(self, key: int, value: int) -> None:
        i = self.hash1(key)
        j = self.hash2(key)
        if self.bucket[i] is None:
            self.bucket[i] = [None] * 1001
        self.bucket[i][j] = value
    def get(self, key: int) -> int:
        i = self.hash1(key)
        j = self.hash2(key)
        if self.bucket[i] is not None:
            if self.bucket[i][j]is not None:
                return self.bucket[i][j]
        return -1

    def remove(self, key: int) -> None:
        i = self.hash1(key)
        j = self.hash2(key)
        if self.bucket[i] is not None:
            if self.bucket[i][j] is not None:
                self.bucket[i][j] = None
        else:
            return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
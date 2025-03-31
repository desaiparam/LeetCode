class TrieNode():
    def __init__(self):
        self.arr = [None] * 26
        self.value = 0
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key: str, val: int) -> None:
        newVal = val
        if key in self.keys:
            newVal = val - self.keys[key]
        self.keys[key] = val
        node = self.root
        for i in key:
            index = ord(i) - ord('a')
            if not node.arr[index]:
                node.arr[index] = TrieNode()
            node = node.arr[index]
            node.value += newVal
            # new = node.value
            # print(new)
            # if newVal is not None:
            #     node.value = val + newVal
            # else:
            #     node.value = val 
            print(node.value)
        # return 
    def sum(self, prefix: str) -> int:
        node = self.root
        # near = None
        for i in prefix:
            index = ord(i) - ord('a')
            if not node.arr[index]:
                return 0
            node = node.arr[index]
        return node.value
        #     if node.arr[index] is None:
        #         break
        #     node = node.arr[index]
        #     if node.value is not None:
        #         near = node.value
        #         # print(near)
        # return near
        # return None
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
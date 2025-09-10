#This is using some thing named OrderedDict in built python dict with changes to O(1)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ord = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.ord:
            self.ord.move_to_end(key,last=True)
            return self.ord[key]
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.ord:
            self.ord[key] = value
            self.ord.move_to_end(key,last = True)
        else:
            self.ord[key] = value
            if len(self.ord) > self.capacity:
                self.ord.popitem(last = False)
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
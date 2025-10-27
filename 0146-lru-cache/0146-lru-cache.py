class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.map = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        

    def addToHead(self,node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.addToHead(node)
            return node.val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.addToHead(node)
        else:
            if len(self.map) == self.size:
                last = self.tail.prev
                self.remove(last)
                del self.map[last.key]
            newNode = Node(key,value)
            self.addToHead(newNode)
            self.map[key] = newNode
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
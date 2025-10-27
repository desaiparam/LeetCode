class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.freq = 1
        self.prev = None
        self.next = None
class DDL:
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.prev = None
        node.next = None
        self.size -= 1
    def addToHead(self,node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        self.size += 1

class LFUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.map = {}
        self.freqMap = {}
        self.minFreq = 0

    
    def update(self,node):
        oldFreq = node.freq
        oldFreqList = self.freqMap[oldFreq]
        oldFreqList.remove(node)
        if oldFreq == self.minFreq and oldFreqList.size == 0:
            self.minFreq += 1
        newFreq = oldFreq + 1
        node.freq = newFreq
        newFreqList = self.freqMap.get(newFreq,DDL())
        newFreqList.addToHead(node)
        self.freqMap[newFreq] = newFreqList

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.update(node)
            return node.val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.update(node)
        else:
            if len(self.map) == self.size:
                minFreqList = self.freqMap[self.minFreq]
                last = minFreqList.tail.prev
                minFreqList.remove(last)
                del self.map[last.key]
            newNode = Node(key,value)
            # self.addToHead(newNode)
            self.map[key] = newNode
            self.minFreq = 1
            freqList = self.freqMap.get(self.minFreq,DDL())
            freqList.addToHead(newNode)
            self.freqMap[self.minFreq] = freqList 
 
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
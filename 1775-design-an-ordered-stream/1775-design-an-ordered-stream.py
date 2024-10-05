class OrderedStream:

    def __init__(self, n: int):
        # print(n)
        # self.OrderedStream = [i for i in range(1,n+1)]
        self.OrderedStream = [None] * n
        self.nextId = 0
        # pass

    def insert(self, idKey: int, value: str) -> List[str]:
        # print("idKey,value",idKey,value)
        
        self.OrderedStream[idKey - 1] = value
        # self.OrderedStream.insert(idKey,value)
        # print(self.OrderedStream)
        ans = []
        while self.nextId < len(self.OrderedStream) and self.OrderedStream[self.nextId] is not None:
            # print("self.nextId",self.nextId)
            # print("self.OrderedStream",self.OrderedStream)
            ans.append(self.OrderedStream[self.nextId])
            # print("ans",ans)
            self.nextId += 1
        return ans
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
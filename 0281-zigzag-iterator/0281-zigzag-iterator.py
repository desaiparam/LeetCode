class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.point1 = 0
        self.point2 = 0
        self.pointRe1 = True 
        

    def next(self) -> int:
        while True:
            if self.pointRe1 :
                if self.point1 < len(self.v1):
                    val = self.v1[self.point1]
                    self.point1 += 1
                    self.pointRe1 = False
                    return val
                self.pointRe1 = False
            else:
                if self.point2 < len(self.v2):
                    val = self.v2[self.point2]
                    self.point2 += 1
                    self.pointRe1 = True
                    return val
                self.pointRe1 = True



    def hasNext(self) -> bool:
        return self.point1 < len(self.v1) or self.point2 < len(self.v2)

        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
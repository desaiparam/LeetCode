# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [nestedList]
        self.idx = [0]
        self.nextel = None
        
    
    def next(self) -> int:
        return self.nextel.getInteger()
        
    
    def hasNext(self) -> bool:
        while self.stack:
            if len(self.stack[-1]) == self.idx[-1]:
                self.stack.pop()
                self.idx.pop()
            else:
                curr = self.stack[-1]
                currIdx = self.idx.pop()
                self.idx.append(currIdx + 1)
                self.nextel = curr[currIdx]
                if self.nextel.isInteger():
                    return True
                else:
                    self.stack.append(self.nextel.getList())
                    self.idx.append(0)
        return False



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
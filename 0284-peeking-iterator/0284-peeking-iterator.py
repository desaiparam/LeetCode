# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        if iterator.hasNext():
              self.nextElement = iterator.next()
        
        

    def peek(self):
        return self.nextElement

    def next(self):
        result = self.nextElement
        if self.hasNext():
              self.nextElement = self.iterator.next()
        return result

    def hasNext(self):
        print(self.nextElement)
        if self.nextElement != -100000:
            return True
        return False 
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
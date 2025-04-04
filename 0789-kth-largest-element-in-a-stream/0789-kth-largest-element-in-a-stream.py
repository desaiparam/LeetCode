import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stack = []
        self.k = k
        for i in nums:
            self.add(i)
        print(self.stack)
        

    def add(self, val: int) -> int:
        if len(self.stack) < self.k or self.stack[0] < val:
            heapq.heappush(self.stack,val)
            if len(self.stack) > self.k:
                heapq.heappop(self.stack)
        return self.stack[0]
        


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
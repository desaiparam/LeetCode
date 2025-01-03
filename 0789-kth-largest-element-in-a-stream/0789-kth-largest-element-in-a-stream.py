import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.newN = [-num for num in nums]
        self.newN = []
        self.k = k
        # heapq.heapify(self.newN)
        for n in nums:
            self.add(n)
        # print("k",self.k)
        # print("newN",self.newN)

    def add(self, val: int) -> int:
        # print("val",val)
        if len(self.newN) < self.k or self.newN[0] < val :
            heapq.heappush(self.newN,val)
            # print("newN in add",self.newN)
            if len(self.newN) > self.k:
                heapq.heappop(self.newN)
                # print("newN in pop",self.newN)/
        return self.newN[0]
            # print("check len - k",len(self.newN)-self.k)
            # print(self.newN[(len(self.newN)-self.newK)])
        # print(self.newN[self.newK])


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
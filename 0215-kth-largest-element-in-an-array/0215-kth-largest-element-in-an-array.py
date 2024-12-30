import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newN = [-num for num in nums]
        heapq.heapify(newN)
        print(newN)
        # finalI = 0
        while k != 1:
            pop = heapq.heappop(newN)
            print(pop)
            # finalI = newN[0] * -1
            print(newN[0])
            k-=1
        # return finalI
        return (newN[0] * -1)
        # print(newN[0] * -1)
        
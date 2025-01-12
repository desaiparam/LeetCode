import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Solution 1
        # newN = [-num for num in nums]
        # heapq.heapify(newN)
        # print(newN)
        # # finalI = 0
        # while k != 1:
        #     pop = heapq.heappop(newN)
        #     print(pop)
        #     # finalI = newN[0] * -1
        #     print(newN[0])
        #     k-=1
        # # return finalI
        # return (newN[0] * -1)
        # # print(newN[0] * -1)

        #Solution 2
        min_h = []
        for num in nums:
            heapq.heappush(min_h,num)
            if len(min_h) > k:
                heapq.heappop(min_h)
        return min_h[0]
        
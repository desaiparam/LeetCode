import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        newN = [-num for num in stones]
        heapq.heapify(newN)
        print(newN)
        while len(newN) != 1:
            fpop = heapq.heappop(newN)
            # print(newN)
            spop = heapq.heappop(newN)
            # spop = 
            # # spop = newN.pop(len(newN)-1)
            print("fpop",fpop)
            print("spop",spop)
            print("sub",fpop-spop)
            heapq.heappush(newN,fpop-spop)
            print("NEW",newN)
            # print(fpop-spop)
        print(newN)
        return -newN[0]
        
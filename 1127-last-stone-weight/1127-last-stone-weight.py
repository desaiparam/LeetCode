import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #SOLUTION 1
        newN = [-num for num in stones]
        heapq.heapify(newN)
        # print(newN)
        while len(newN) != 1:
            fpop = heapq.heappop(newN)
            # print(newN)
            spop = heapq.heappop(newN)
            # spop = 
            # # spop = newN.pop(len(newN)-1)
            # print("fpop",fpop)
            # print("spop",spop)
            # print("sub",fpop-spop)
            heapq.heappush(newN,fpop-spop)
            # print("NEW",newN)
            # print(fpop-spop)
        # print(newN)
        return -newN[0]
        

        #SOLUTION 2
        # stones = [-s for s in stones]
        # heapq.heapify(stones)
        # # print(stones)
        # while len(stones) > 1:
        #     f = heapq.heappop(stones)
        #     s = heapq.heappop(stones)
        #     if s > f: 
        #         # print(f-s)
        #         heapq.heappush(stones,f-s)
        # stones.append(0)
        # print(stones[0])
        # return -stones[0]
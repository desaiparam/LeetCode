import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        #SOLUTION 1 
        # if len(sticks) == 1:
        #     return 0 
        # heapq.heapify(sticks)
        # cost = 0
        # while len(sticks) != 2:
        #     f_s = heapq.heappop(sticks)
        #     s_s = heapq.heappop(sticks)
        #     cost = cost +f_s + s_s
        #     heapq.heappush(sticks,f_s+s_s)
        # #     print(sticks)
        # # print(sticks)
        # # print(cost)
        # final = heapq.heappop(sticks)
        # finals = heapq.heappop(sticks)
        # # print(final)
        # # print(finals)
        # # print(cost+finals+final)
        # return cost+finals+final
        
        #SOLUTION 2
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            f_s = heapq.heappop(sticks)
            s_s = heapq.heappop(sticks)
            cost += (f_s + s_s)
            heapq.heappush(sticks,f_s+s_s)

        return cost
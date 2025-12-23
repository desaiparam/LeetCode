class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:(x[0],x[-1]))
        minheap =[]
        best = 0
        ans = 0
        for start,end,value in events:
            while minheap and minheap[0][0] < start:
                lastend,val = heapq.heappop(minheap) 
                best = max(best,val)
            heapq.heappush(minheap,(end,value))
            ans = max(ans,best+value)
        return ans
        
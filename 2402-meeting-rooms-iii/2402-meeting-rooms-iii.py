class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        minheap = []
        available = [i for i in range(n)]
        heapq.heapify(available)
        counter = [0] * n
        for start,end in meetings:
            while minheap and minheap[0][0] <= start:
                _,room = heapq.heappop(minheap)
                heapq.heappush(available,room)
            if not available:
                endtime,room = heapq.heappop(minheap)
                endtime += end-start
                heapq.heappush(minheap,(endtime,room))
                counter[room] += 1
            elif available:
                room = heapq.heappop(available)
                heapq.heappush(minheap,(end,room))
                counter[room] += 1
        return counter.index(max(counter))


            

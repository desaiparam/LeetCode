import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0 :
            return -1
        intervals.sort(key=lambda x:x[0])
        minHeap = []
        for start,end in intervals:
            if minHeap and start >= minHeap[0]:
                heapq.heapreplace(minHeap,end)
            else:
                heapq.heappush(minHeap,end)
        return len(minHeap)
        
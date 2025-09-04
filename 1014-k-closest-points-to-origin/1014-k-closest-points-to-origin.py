class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i,j in points:
            dis = sqrt((i**2)+ (j**2))
            if len(heap) < k:
                heapq.heappush(heap,(-dis,i,j))
            else:
                if -heap[0][0] > dis:
                    heapq.heapreplace(heap,(-dis,i,j))
        return [[x,y] for _,x,y in heap]
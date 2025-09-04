class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for i,j in points:
            dis = sqrt((i**2)+ (j**2))
            heapq.heappush(heap,(dis,i,j))
        print(heap)
        for _ in range(k):
            dis,i,j = heapq.heappop(heap)
            res.append((i,j))
        return res
            
        
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
        ed = []
        for i in points:
            # print(i[0],i[1])
            minH.append((i, math.sqrt(i[0] ** 2 + i[1] ** 2)))
            # heapq.heappush(minH,sqrt((i[0] - 0) ** 2 + (i[1] - 0) ** 2))
            # print(minH.heappush(sqrt((i[0] - 0) ** 2 + (i[1] - 0) ** 2)))
        # heapq.heapify(minH)
        # print(minH)
        heap = [(distance, point) for point, distance in minH]
        heapq.heapify(heap)
        # print(heap)
        while k > 0:
            # heapq.heapify(minH)
            c, ed1  = heapq.heappop(heap)
            ed.append(ed1)
            # print(ed)
            # print(c)
            k -= 1
        return ed
        # return 
        
        
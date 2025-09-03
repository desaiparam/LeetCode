class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        print(freq)
        heap = []
        for i,j in freq.items():
            heapq.heappush(heap,(j,i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for (val,key) in heap]

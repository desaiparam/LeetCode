class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n+1)
        for i in citations:
            if i > n:
                buckets[n] +=1
            else:
                buckets[i] += 1
        sumy = 0
        for i in range(n,-1,-1):
            sumy += buckets[i]
            if sumy >= i:
                return i
        return -1



        
        
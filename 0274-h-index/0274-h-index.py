class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        for i ,j in enumerate(citations):
            if n-i <= j:
                return n-i
        return 0
        
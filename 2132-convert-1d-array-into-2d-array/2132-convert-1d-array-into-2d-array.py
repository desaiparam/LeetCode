class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m*n != len(original):
            return []
        res = [[] for _ in range(m)]
        for i in range(m):
            res[i] = original[i * n: i*n + n]
        return res
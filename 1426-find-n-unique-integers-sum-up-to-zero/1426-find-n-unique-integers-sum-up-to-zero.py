class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        midlle = n >> 1
        
        for _ in range(midlle):
            res.append(midlle)
            res.append(-midlle)
            midlle-=1
        if n & 1:
            res.append(0)
        return res
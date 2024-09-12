class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # res = [[0] *n for _ in range(m)]
        # # fd= n-1
        # # sd = 2*n-1
        # if len(original) !=m*n:
        #     return []
        # for i in range(len(original)):
        #     res[i//n][i%n] = original[i]
        # return res
        if m*n != len(original):
            return []
        res = [[] for _ in range(m)]
        for i in range(m):
            res[i] = original[i * n: i*n + n]
        return res
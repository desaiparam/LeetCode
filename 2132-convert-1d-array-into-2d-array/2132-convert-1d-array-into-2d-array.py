class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = [[0] *n for _ in range(m)]
        if len(original) !=m*n:
            return []
        for i in range(len(original)):
            res[i//n][i%n] = original[i]
        return res
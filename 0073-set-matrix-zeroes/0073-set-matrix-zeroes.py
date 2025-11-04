class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        setR = set()
        setC = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    setR.add(i)
                    setC.add(j)
        for i in range(n):
            for j in range(m):
                if i in setR or j in setC:
                    matrix[i][j] = 0
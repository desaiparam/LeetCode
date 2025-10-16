class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxy = 0
        # dp = [[0] *(n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j] == "1":
                    if i == m-1 or j == n-1:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 1 + min(int(matrix[i][j+1]),min(int(matrix[i+1][j]),int(matrix[i+1][j+1])))
                    maxy = max(maxy,matrix[i][j])
        return maxy*maxy
                        

                
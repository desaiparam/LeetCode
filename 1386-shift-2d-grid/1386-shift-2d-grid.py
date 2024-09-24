class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        n = len(grid)
        m = len(grid[0])
        v = [0]*n*m
        k = k % (n*m)
        for i in range(n):
            for j in range(m):
                v[i*m+j] = grid[i][j]
        v = v[-k:] + v[:-k]
        for i in range(n):
            for j in range(m):
                grid[i][j] = v[i * m + j ]
            
        return grid

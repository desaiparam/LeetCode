class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c):
            if 0 > r or r >= n or 0 > c or c >= m or grid[r][c] == 0:
                return 
            grid[r][c] = 0
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        for i in range(m):
            if grid[0][i] == 1:
                dfs(0,i)
            if grid[n-1][i] == 1:
                dfs(n-1,i)
        for j in range(n):
            if grid[j][0] == 1:
                dfs(j,0)
            if grid[j][m-1] == 1:
                dfs(j,m-1)
        return sum(cell for row in grid for cell in row)        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        maxy = 0
        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return 0
            if grid[r][c] == 0 or visited[r][c]:
                return 0
            visited[r][c] = True
            area = 1
            area += dfs(r,c+1)
            area += dfs(r+1,c)
            area += dfs(r,c-1)
            area += dfs(r-1,c)
            return area
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    maxy = max(maxy,dfs(i,j))
        return maxy


        
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pac = [[False] * m for _ in range(n)]
        alt = [[False] * m for _ in range(n)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        res = []
        def dfs(r,c,seen):
            seen[r][c] = True
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and heights[nr][nc] >= heights[r][c] and not seen[nr][nc]:
                    dfs(nr,nc,seen)
        for i in range(m):
            dfs(0,i,pac)
        for j in range(n):
            dfs(j,0,pac)
        for i in range(m):
            dfs(n-1,i,alt)
        for j in range(n):
            dfs(j,m-1,alt)
        for i in range(n):
            for j in range(m):
                if pac[i][j] and alt[i][j]:
                    res.append([i,j])
        return res
        
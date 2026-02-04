class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        n = len(grid)
        m = len(grid[0])
        def dfs(r,c,parentrow,parentcol):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            visited.add((r,c))
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if grid[nr][nc] == grid[r][c]:
                        if (nr,nc) == (parentrow,parentcol):
                            continue
                        if (nr,nc) in visited:
                            return True
                        if dfs(nr,nc,r,c):
                            return True

            return False
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited:
                    if dfs(i,j,-1,-1):
                        return True
        return False
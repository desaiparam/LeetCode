class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] != 0 or grid[n-1][m-1] != 0:
            return -1
        visited = [[False] *m for _ in range(n)]
        q = deque([(0,0,1)])
        direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        count = 0
        while q:
            r,c,level = q.popleft()
            if r == n-1 and c == m-1:
                return level
            for dr,dc in direction:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr,nc,level+1))

        return -1


        
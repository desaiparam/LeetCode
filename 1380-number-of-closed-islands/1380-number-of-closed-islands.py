class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        q = deque()
        number = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and not visited[i][j]:
                    visited[i][j] = True
                    q.append((i,j))
                    closed = True
                    while q:
                        r,c  = q.popleft()
                        if r == 0 or r == n -1 or c == 0 or c == m-1:
                            closed = False
                        for dr,dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr <n and 0 <= nc < m and grid[nr][nc] == 0 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr,nc))
                    if closed:
                        number += 1
                
        return number


        
        
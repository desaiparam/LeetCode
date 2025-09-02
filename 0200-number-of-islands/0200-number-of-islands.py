class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        q = deque()
        number = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    number += 1
                    q.append((i,j))
                    while q:
                        r,c  = q.popleft()
                        for dr,dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr <n and 0 <= nc < m and grid[nr][nc] == '1' and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr,nc))
        return number


        
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        q = deque()
        def mark(sr,sc):
            stack = [(sr,sc)]
            grid[sr][sc] = 2
            q.append((sr,sc))
            while stack:
                r,c = stack.pop()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0<= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        grid[nr][nc] =2
                        stack.append((nr,nc)) 
                        q.append((nr,nc)) 
        found = False
        for i in range(n):
            for j in range(m):
                if found:
                    break
                if grid[i][j] == 1:
                    mark(i,j)
                    found = True
                    break
        level = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m :
                        if grid[nr][nc] == 1:
                            return level
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = -1
                            q.append((nr,nc)) 
            level += 1
        return -1




        
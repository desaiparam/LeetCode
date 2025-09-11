class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        mint = 0
        vis = [[False] * len(grid[0]) for _ in range(len(grid))]
        startPoint = [] 
        dirc = [(1,0),(0,1),(0,-1),(-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    startPoint.append((i, j))
                    vis[i][j] = True
        q = deque(startPoint)
        while q:
            foundNew = False
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr , dc in dirc:
                    nr = i + dr
                    nc = j + dc
                    if 0<= nr < n and 0 <= nc < m:
                        if grid[nr][nc] == 1 and not vis[nr][nc]:
                            grid[nr][nc] = 2
                            vis[nr][nc] = True
                            q.append((nr,nc))
                            foundNew  = True
            if foundNew:
                mint += 1  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return mint

        
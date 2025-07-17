class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mint = 0
        vis = [[False] * len(grid[0]) for _ in range(len(grid))]
        startPoint = []
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
                for dirX , dirY in [(1,0),(0,1),(0,-1),(-1,0)]:
                    ni ,nj = i + dirX,j+dirY
                    if 0<= ni <len(grid) and 0 <= nj < len(grid[0]):
                        if grid[ni][nj] == 1 and not vis[ni][nj]:
                            grid[ni][nj] = 2
                            vis[ni][nj] = True
                            q.append((ni,nj))
                            foundNew  = True
            if foundNew:
                mint += 1  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return mint

        
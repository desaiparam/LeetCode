class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        mint = 0
        vis = [[False] * len(grid[0]) for _ in range(len(grid))] #visited array with false
        startPoint = [] # to append in the queue to know where to start from 
        dirc = [(1,0),(0,1),(0,-1),(-1,0)] #the four directions
        # to find first starting point to append in the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    startPoint.append((i, j))
                    vis[i][j] = True
                    # break
        q = deque(startPoint)

        while q:
            foundNew = False
            for _ in range(len(q)):
                i,j = q.popleft()
                # check four directions 
                for dr , dc in dirc:
                    nr = i + dr
                    nc = j + dc
                    if 0<= nr < n and 0 <= nc < m:
                        # if fresh orange found and visited is false
                        if grid[nr][nc] == 1 and not vis[nr][nc]:
                            grid[nr][nc] = 2
                            vis[nr][nc] = True
                            q.append((nr,nc))
                            foundNew  = True
            #this is written here to increment the timer 
            if foundNew:
                mint += 1  
        # in the end if any fresh orange is remaning we will return -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return mint

        
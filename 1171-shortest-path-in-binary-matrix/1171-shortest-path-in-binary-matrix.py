class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        if grid[n-1][m-1] == 1 or grid[0][0] == 1:
            return -1
        q = deque([(0,0)])
        grid[0][0] = 1
        directions = [
    (1, 0),   # down
    (-1, 0),  # up
    (0, 1),   # right
    (0, -1),  # left
    (1, 1),   # down-right
    (-1, -1), # up-left
    (1, -1),  # down-left
    (-1, 1)   # up-right
]

        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))
        return grid[n-1][m-1] if grid[n-1][m-1] != 0  else  -1



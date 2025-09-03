class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        heap = [(0,start[0],start[1])]
        best = [[float('inf')] * m for _ in range(n)]
        best[start[0]][start[1]] = 0
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        while heap:
            dist , r,c = heapq.heappop(heap)
            if dist > best[r][c]:
                continue 
            if (r, c) == (destination[0], destination[1]):
                return dist
            for dr,dc in direction:
                    step = 0
                    nr = r
                    nc = c
                    while 0 <= nr+dr < n and 0 <= nc+dc < m and maze[nr+dr][nc+dc] == 0:
                        nr += dr
                        nc += dc
                        step += 1
                    new_dist = step + dist
                    if new_dist < best[nr][nc]:
                        best[nr][nc] = new_dist
                        heapq.heappush(heap,(new_dist,nr,nc))
        return -1
                

            

        

        
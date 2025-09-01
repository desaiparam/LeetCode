class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entR,entC = entrance
        R = len(maze)
        C = len(maze[0])
        visited = [[False]*C for _ in range(R)]
        q = deque([(entR,entC,0)])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            # print(q)
            r,c,d = q.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and  0 <= nc < C and maze[nr][nc] == '.' and not visited[nr][nc]:
                    if (nr == 0 or nr == R-1 or nc == 0 or nc == C-1) and not (nr == entR and nc == entC):
                        return d + 1
                        
                    visited[nr][nc] = True
                    q.append((nr,nc,d+1))
                    
        return -1


        
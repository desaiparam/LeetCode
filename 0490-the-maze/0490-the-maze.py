class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque([(start[0], start[1])]) 
        maze[start[0]][start[1]] = 2
        while q:
            r,c = q.popleft()
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                while nr < m and nr >= 0 and nc < n and nc >= 0 and maze[nr][nc] != 1:
                    nr += dr
                    nc += dc
                nr -= dr
                nc -= dc
                if nr == destination[0] and nc == destination[1]:
                    return True
                if maze[nr][nc] != 2:
                    q.append((nr,nc))
                    maze[nr][nc] = 2
        return False

                

        
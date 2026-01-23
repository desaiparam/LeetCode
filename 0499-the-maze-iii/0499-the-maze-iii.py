class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        n = len(maze)
        m = len(maze[0])
        heap = [(0,"",ball[0],ball[1])]
        best = [[(float('inf'), "") for _ in range(m)] for _ in range(n)]
        best[ball[0]][ball[1]] = (0, "")
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        while heap:
            dist,way,r,c = heapq.heappop(heap)
            if dist > best[r][c][0]:
                continue
            if (r,c) == (hole[0],hole[1]):
                return way
            for dr,dc in direction:
                nr = r 
                nc = c 
                step = 0
                newway = way
                if (dr,dc) == (0,1):
                    newway +="r"
                if (dr,dc) == (0,-1):
                    newway +="l"
                if (dr,dc) == (1,0):
                    newway +="d"
                if (dr,dc) == (-1,0):
                    newway +="u"
                print(newway)
                while 0 <= nr+ dr < n and 0 <= nc+ dc < m and maze[nr+dr][nc+dc] == 0:
                    nr += dr
                    nc += dc
                    step += 1
                    if (nr,nc) == (hole[0],hole[1]):
                        break
                if step == 0:
                    continue
                new_d = step + dist
                if (new_d < best[nr][nc][0]) or (new_d == best[nr][nc][0] and newway<best[nr][nc][1]):
                    best[nr][nc] = (new_d,newway)
                    heapq.heappush(heap,(new_d,newway,nr,nc))
                # elif new_d == best[nr][nc] and newway 
        return "impossible"

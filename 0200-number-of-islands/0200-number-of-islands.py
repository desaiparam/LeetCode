class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        que = deque()
        visi = set()
        nu = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visi:
                    nu +=1
                    que.append((i,j))
                    visi.add((i, j))
                    # print(que)
                    # print(visi)
                while que:
                    c,k = que.popleft()
                    for x,y in directions:
                        nx,ny = x+c,y+k
                        if 0 <= nx <len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1" and (nx,ny) not in visi:
                            que.append((nx,ny))
                            visi.add((nx,ny))

        return nu

        
        
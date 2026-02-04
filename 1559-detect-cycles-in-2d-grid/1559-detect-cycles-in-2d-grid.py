class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # visited = set()
        # n = len(grid)
        # m = len(grid[0])
        # def dfs(r,c,parentrow,parentcol):
        #     directions = [(1,0),(-1,0),(0,1),(0,-1)]
        #     visited.add((r,c))
        #     for dr,dc in directions:
        #         nr = r + dr
        #         nc = c + dc
        #         if 0 <= nr < n and 0 <= nc < m:
        #             if grid[nr][nc] == grid[r][c]:
        #                 if (nr,nc) == (parentrow,parentcol):
        #                     continue
        #                 if (nr,nc) in visited:
        #                     return True
        #                 if dfs(nr,nc,r,c):
        #                     return True

        #     return False
        # for i in range(n):
        #     for j in range(m):
        #         if (i,j) not in visited:
        #             if dfs(i,j,-1,-1):
        #                 return True
        # return False
        n = len(grid)
        m = len(grid[0])
        parent = list(range(n*m))
        rank = [0] * (n*m)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True
        def idx(r,c):
            return r * m+ c
        for i in range(n):
            for j in range(m):
                if i + 1 < n and grid[i][j] == grid[i+1][j]:
                    if not union(idx(i,j),idx(i+1,j)):
                        return True
                if j + 1 < m and grid[i][j] == grid[i][j+1]:
                    if not union(idx(i,j),idx(i,j+1)):
                        return True
        return False
                    


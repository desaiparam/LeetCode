class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        # print(mat)
        while q:
            r , c  = q.popleft()
            for dr,dc in direction:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == -1:
                    # print(mat)
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr,nc))
        return mat


        
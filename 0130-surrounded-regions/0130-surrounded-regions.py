class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        q = deque()
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        for i in range(m):
            if board[0][i] == "O":
                board[0][i] = "T"
                q.append((0,i))
        for i in range(m):
            if board[n-1][i] == "O":
                board[n-1][i] = "T"
                q.append((n-1,i))
        for i in range(n):
            if board[i][0] == "O":
                board[i][0] = "T"
                q.append((i,0))
        for i in range(n):
            if board[i][m-1] == "O":
                board[i][m-1] = "T"
                q.append((i,m-1))
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "O":
                    q.append((nr,nc))
                    board[nr][nc] = "T"
        for i in range(n):
            for j in range(m):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

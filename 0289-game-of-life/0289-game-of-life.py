class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
        def counter(r,c):
            count = 0
            for dr,dc in directions:
                nr = r +dr
                nc = c +dc
                if 0<= nr < n and 0 <= nc < m:
                    if board[nr][nc] == 1 or board[nr][nc] == 2:
                        count += 1
            return count
        for i in range(n):
            for j in range(m):
                count = counter(i,j)
                if board[i][j] == 1  and ( count < 2 or count >3):
                    board[i][j] = 2
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 3 
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 1

        
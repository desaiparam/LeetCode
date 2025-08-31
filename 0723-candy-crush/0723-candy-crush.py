class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n = len(board)
        m = len(board[0])
        while True:
            marked = False
            for i in range(n):
                j = 0
                while j < m-2:
                    v = abs(board[i][j])
                    if v != 0 and abs(board[i][j+1]) == v and abs(board[i][j+2]) == v:
                        marked = True
                        k = j
                        while k < m and abs(board[i][k]) == v:
                            board[i][k] = -v
                            k += 1
                        j = k
                    else:
                        j += 1
            for j in range(m):
                i = 0
                while i < n - 2:
                    v = abs(board[i][j])
                    if v != 0 and abs(board[i+1][j]) == v and abs(board[i+2][j]) == v:
                        marked = True
                        k = i
                        while k < n and abs(board[k][j]) == v:
                            board[k][j] = -v
                            k += 1
                        i = k
                    else:
                        i += 1
            if not marked:
                return board

            for i in range(n):
                for j in range(m):
                    if board[i][j] < 0:
                        board[i][j] = 0
            for j in range(m):
                write = n -1
                for i in range(n-1,-1,-1):
                    if board[i][j] > 0:
                        board[write][j] = board[i][j]
                        write -= 1
                for i in range(write,-1,-1):
                    board[i][j] = 0
 
                
 

        
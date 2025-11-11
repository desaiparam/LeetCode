class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = len(board)
        m = len(board[0])
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        q = deque([(click[0],click[1])])
        board[click[0]][click[1]] = 'B'
        directions = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                count = 0
                for dr,dc in directions:
                    nr = dr + r
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 'M':
                        count += 1
                if count > 0:
                    board[r][c] = str(count)
                else:
                    for dr,dc in directions:
                        nr = dr + r
                        nc = c + dc
                        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 'E':
                            q.append((nr,nc))
                            board[nr][nc] = 'B'
        return board
                    




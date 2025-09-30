class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [(1,0),(0,1),(0,-1),(-1,0)]
        def dfs(i,j,idx):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i == m or j == n or board[i][j] == "#":
                return False
            if board[i][j] != word[idx]:
                return False
            board[i][j] = "#"
            for dr,dc in dirs:
                nr = dr + i
                nc = dc + j
                if dfs(nr,nc,idx+1):
                    return True
            board[i][j] = word[idx]
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False

        
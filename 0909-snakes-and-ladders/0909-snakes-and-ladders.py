class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        q = deque([0])
        lvl = 0
        def getId(idx):
            r = idx // n
            c = idx % n
            if r % 2 == 0:
                return n-r-1,c
            else:
                return n-r-1,n-c-1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for i in range(1,7):
                    nidx = curr + i
                    r,c = getId(nidx)
                    if nidx == n * n - 1 or board[r][c] == n*n:
                        return lvl + 1
                    if board[r][c] != -2:
                        if board[r][c] == -1:
                            q.append(nidx)
                        else:
                            q.append(board[r][c] - 1)
                        board[r][c] = -2
            lvl += 1
        return -1 
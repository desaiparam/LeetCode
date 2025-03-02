class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        m = len(board)
        n = len(board[0])
        q = deque()
        q.append(click)
        visit = set()
        # visit
        # visit.add(tuple(click))
        while q:
            for _ in range(len(q)):
                # print("q",q)
                current = q.popleft()
                x,y = current[0] , current[1]
                count_mine = 0
                for a,b, in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,1),(1,-1)]:
                    # print("a,b",a,b)
                    nx,ny = x+a,y+b
                    # print("nx",nx)
                    # print("ny",ny)

                    if 0 <= nx < m and 0 <= ny < n:
                        # print("a,b",a,b)
                        # print("board",board[nx][ny])
                        if board[nx][ny] == 'M':
                            count_mine += 1 
                if count_mine > 0:
                    # print(board[x][y])
                    board[x][y] = str(count_mine)
                else:
                    # print("board[x][y] before",board[x][y])
                    board[x][y] = 'B'
                    for a,b in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,1),(1,-1)]:
                        nx ,ny = x+a,y+b 
                        # print("nx",nx)
                        # print("ny",ny)    
                        if 0 <= nx <m and 0 <= ny < n and (nx,ny) not in visit:
                            q.append([nx,ny])
                            visit.add((nx,ny))
                        # print("q after",q)
                        # print("visit",visit)
                        # print("board[x][y] after",board[x][y])
        return board
                    

        
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
                #TC O(9^N^2)where even n will be 9 so if i have a contant 9*9 i can say O(1) as input will not affect the time complexity
        seenSmallerMatrix = defaultdict(set)
        seenRow = defaultdict(set)
        seenCol = defaultdict(set)
        for i in range(9): 
            for j in range(9): 
                if board[i][j] == ".": 
                    continue
                seenRow[i].add(board[i][j]) 
                seenCol[j].add(board[i][j]) 
                seenSmallerMatrix[(i//3,j//3)].add(board[i][j])
        def filler(i,j):
            if i == 9:
                return True
            if j == 9:
                return filler(i+1,0)
            if board[i][j] == ".":
                for val in range(1,10):
                    if isSafe(str(val),i,j):
                        board[i][j] = str(val)
                        seenRow[i].add(str(val))
                        seenCol[j].add(str(val))
                        seenSmallerMatrix[(i//3,j//3)].add(str(val))
                        if filler(i,j+1):
                            return True
                        board[i][j] = "."
                        seenRow[i].remove(str(val))
                        seenCol[j].remove(str(val))
                        seenSmallerMatrix[(i//3, j//3)].remove(str(val))
            else:
                return filler(i,j+1)
            return False
        def isSafe(val,i,j):
            if val in seenRow[i] or val in seenCol[j] or val in seenSmallerMatrix[(i//3,j//3)]:
                return False
            return True
        filler(0,0)


        
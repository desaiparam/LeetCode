class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [[False]*n for _ in range(n)]
        result = []
        def backtrack(grid,r):
            if r == n:
                li = []
                for i in range(n):
                    sb = []
                    for j in range(n):
                        if grid[i][j]:
                            sb.append("Q")
                        else:
                            sb.append(".")
                    li.append("".join(sb))
                result.append(li)
                return 
                    
            for c in range(n):
                if isSafe(grid,r,c):
                    grid[r][c] = True
                    backtrack(grid,r+1)
                    grid[r][c] = False
        def isSafe(grid,r,c):
            i = r
            j = c
            while i >=0:
                if grid[i][j]:
                    return False
                i -= 1
            i = r
            j = c
            while i >= 0 and j >= 0:
                if grid[i][j]:
                    return False
                i -= 1
                j -= 1
            i = r
            j = c
            while i >= 0 and j < n :
                if grid[i][j] :
                    return False
                i -= 1
                j += 1
            return True
        backtrack(grid,0)
        return result

        
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        res = [0]*(n*m)
        row = 0
        col = 0
        directions = True
        for i in range(n*m):
            res[i] = mat[row][col]
            if directions:
                if row == 0 and col != m -1:
                    col += 1
                    directions = False
                elif col == m-1:
                    row += 1
                    directions = False
                else:
                    row -= 1
                    col += 1
            else:
                if col == 0 and row != n -1:
                    row += 1
                    directions = True
                elif row == n-1:
                    col += 1
                    directions = True
                else:
                    row += 1
                    col -= 1
                    
        return res
        
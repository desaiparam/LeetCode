class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0  
        for i in range(n-2):
            for j in range(m-2):
                used = [-1] * 10
                valid = True
                for x in range(3):
                    for y in range(3):
                        value = grid[i+x][j+y]
                        if value < 1 or value > 9 or used[value]!=-1:
                            valid = False  
                            break
                        used[value] = value
                    if not valid:
                        break
                sumy = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                for x in range(3):
                    if grid[i+x][j] + grid[i+x][j+1] + grid[i+x][j+2] !=sumy:
                        valid = False
                for x in range(3):
                    if grid[i][j+x] + grid[i+1][j+x] + grid[i+2][j+x] !=sumy:
                        valid = False
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]!=sumy:
                    valid = False
                if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]!=sumy:
                    valid = False
                if valid:
                    ans += 1
        return ans

                

            
        
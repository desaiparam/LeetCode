class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        if len(grid) <= 1:
            # print("ttttt")
            for i in range(len(grid[0])-1):
                if grid[0][i] == grid[0][i+1]:
                    return False
            return True 
        for i in range(len(grid)-1):
            for j in range(len(grid[0])):
                if  grid[i][j] != grid[i+1][j]:
                    print(grid[i][j])  
                    print(grid[i+1][j])
                    print(grid[i][j])  
                    # print(grid[i][j+1])
                    return False
                if j+1 < len(grid[0]) and grid[i][j] == grid[i][j+1]:
                    return False
        return True
        
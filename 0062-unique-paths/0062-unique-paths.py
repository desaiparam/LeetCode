class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def helper(i,j):
            if i == 0 and j == 0:
                return 1 
            if i < 0 or j < 0:
                return 0
            if (i ,j) in memo:
                return memo[(i,j)]
            # case of not taking the left side
            notTake = helper(i,j-1)
            # case of not taking the right side
            take = helper(i-1,j)
            memo[(i,j)] = notTake + take
            return memo[(i,j)]
        return helper(m-1,n-1)
        

        


        
        
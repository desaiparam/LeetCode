class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #TC and SC O(N*M)
        # n = len(obstacleGrid)
        # m = len(obstacleGrid[0])
        # dp = [[0] * (m) for _ in range(n)]
        # dp[n-1][m-1] = 1
        # for i in  range(n-1,-1,-1):
        #     for j in range(m-1,-1,-1):
        #         if obstacleGrid[i][j] == 1:
        #             dp[i][j] = 0
        #         else:
        #             if i < n-1: 
        #                 # print(dp,i,j)
        #                 dp[i][j] += dp[i+1][j]
        #             if j < m-1:
        #                 # print(dp[i][j+1])
        #                 dp[i][j] += dp[i][j+1]
        # return dp[0][0]
        #TC O(N)
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [0] * m
        dp[-1] = 1
        for i in  range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j < m-1: 
                        # print(dp,i,j)
                        dp[j] += dp[j+1]
        return dp[0]

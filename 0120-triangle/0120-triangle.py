class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #TC O(N^2) SC O(N^2)
        # n = len(triangle)
        # memo = {}
        # def helper(i,j):
        #     if i == n-1:
        #         return triangle[i][j]
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     total = triangle[i][j] + min(helper(i+1,j), helper(i+1,j+1))
        #     memo[(i,j)] = total
        #     return total
        # return helper(0,0)
        #TC O(N^2) SC O(N^2)
        # n = len(triangle)
        # dp = [[float('inf')] * (n+1) for _ in range(n+1)]
        # for i in range(n):
        #     dp[n-1][i] = triangle[n-1][i]
        # for i in range(n-2,-1,-1):
        #     for j in range(i+1):
        #         dp[i][j] = triangle[i][j] + min(dp[i+1][j],dp[i+1][j+1])
        # print(dp)
        # return dp[0][0]
        # print(n)
        #TC O(N^2) SC O(N)
        n = len(triangle)
        dp = triangle[-1][:]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
        print(dp)
        return dp[0]
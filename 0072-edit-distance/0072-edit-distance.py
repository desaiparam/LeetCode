class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #TC and sc nm 
        # n = len(word1)
        # m = len(word2)
        # memo = {}
        # def dfs(i,j):
        #     if i == n:
        #         return m - j
        #     if j == m:
        #         return n - i
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if word1[i] == word2[j]:
        #         res = dfs(i+1,j+1)
        #     else:
        #         dele = 1 + dfs(i,j+1)
        #         edit = 1 + dfs(i+1,j+1)
        #         add = 1 + dfs(i+1,j)
        #         res = min(dele,add,edit)
        #         memo[(i,j)] = res
        #     return res
        # return dfs(0,0)
        #TC SC nm
        # n = len(word1)
        # m = len(word2)
        # dp = [[0] * (m+1) for _ in range(n+1)]
        # for i in range(1,m+1):
        #     dp[0][i] = i
        # for i in range(1,n+1):
        #     for j in range(m+1):
        #         if j == 0:
        #             dp[i][j] = i
        #             continue
        #         if word1[i-1] == word2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        # return dp[n][m]
        n = len(word1)
        m = len(word2)
        dp = [j for j in range(m + 1)]
        for i in range(1,n+1):
            dia = dp[0]
            dp[0] = i
            for j in range(1,m+1):
                temp = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = dia
                else:
                    dp[j] = 1 + min(dp[j],dia,dp[j-1])
                dia = temp
        return dp[m]
        
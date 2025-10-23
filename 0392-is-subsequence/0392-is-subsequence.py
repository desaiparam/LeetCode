class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # SOlution 1 two pointers easy solution O(N+M) SC O(1)
        # if len(s) == 0:
        #     return True
        # if len(t) == 0:
        #     return False
        # i = 0
        # j = 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j +=1
        # return i == len(s)
        #Solution 2 DP TC O(N*M) SC O(N*M)
        # n = len(s)
        # m = len(t)
        # dp = [[False]*(m+1) for _ in range(n+1)]
        # for i in range(m+1):
        #     dp[0][i] = True
        # for i in range(1,n+1):
        #     for j in range(1,m+1):
        #         if s[i-1] == t[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = dp[i][j-1]
        # return dp[n][m]
        #Solution 3 DP TC O(N*M) SC O(N)
        n = len(s)
        m = len(t)
        dp = [True] * (m+1)
        # for i in range(m+1):
        #     dp[0][i] = True
        for i in range(1,n+1):
            prev = dp[0]
            dp[0] = False
            for j in range(1,m+1):
                print(dp[j])
                temp = dp[j]
                if s[i-1] == t[j-1]:
                    dp[j] = prev
                else:
                    dp[j] = dp[j-1]
                prev = temp
        return dp[-1]
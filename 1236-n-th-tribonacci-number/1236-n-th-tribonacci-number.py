class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1] * (n+1)
        def helper(n):
            if n == 0:
                return 0
            if n ==1:
                return 1
            if n == 2:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = helper(n-1) + helper(n-2) + helper(n-3)
            return dp[n]
        return helper(n)
        
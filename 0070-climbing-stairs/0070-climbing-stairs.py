class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        def helper(n):
            if n == 0:
                return 1
            if memo[n] != -1:
                return memo[n]
            if n < 0:
                return 0
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        
        return helper(n)
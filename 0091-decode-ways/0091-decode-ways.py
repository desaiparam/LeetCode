class Solution:
    def numDecodings(self, s: str) -> int:
        # TC O(N) SC O(N)
        # n = len(s)
        # memo = {}
        # def helper(i):
        #     if i == n:
        #         return 1
        #     if s[i] == "0":
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     ways = 0
        #     ways += helper(i+1)
        #     if i < n-1 and int(s[i:i+2]) <= 26:
        #         ways += helper(i+2)
        #     memo[i] = ways
        #     return ways
        
        # return helper(0)
        #TC O(N) SC O(N)
        n = len(s)
        dp = [0] * (n +1)
        dp[n] = 1
        for i in range(n-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] += dp[i+1]
            if i < n-1 and 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
            
        return dp[0]
                




        
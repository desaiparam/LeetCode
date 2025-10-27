class Solution:
    def rob(self, nums: List[int]) -> int:
        #TC O(N) SC O(N)
        # n = len(nums)
        # if n == 1 or n == 2:
        #     return max(nums) 
        # memo = {}
        # def helper(i,k):
        #     if i >= k:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     take = nums[i]+helper(i+2,k)
        #     nottake = helper(i+1,k)
        #     print(memo)
        #     memo[i] = max(take,nottake)
        #     return memo[i]
        # linear = helper(0,n-1)
        # memo = {}
        # circular = helper(1,n)
        # return max(linear,circular)
        #TC O(N) SC O(N)
        n = len(nums)
        if n == 1 or n == 2:
            return max(nums) 
        dp = [0] * (n+1)
        dp[n-2] = nums[n-2]
        for i in range(n-3,-1,-1):
            dp[i] = max(nums[i]+dp[i+2],dp[i+1])
        linear1 = dp[0]
        dp = [0] * (n+1)
        dp[n-1] = nums[n-1]
        for i in range(n-2,0,-1):
            dp[i] = max(nums[i]+dp[i+2],dp[i+1])
        linear2 = dp[1]
        return max(linear1,linear2)
        
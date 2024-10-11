class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(0,i):
                if i <= j + nums[j]:
                    dp[i] = min(dp[i],dp[j]+1)
        return dp[-1]
        
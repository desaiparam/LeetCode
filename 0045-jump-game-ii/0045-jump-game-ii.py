class Solution:
    def jump(self, nums: List[int]) -> int:
        #TC O(N^2)
        # if len(nums) == 1:
        #     return 0
        # n = len(nums)
        # dp = [float('inf')] * n
        # dp[-1] = 0
        # for i in range(n-2,-1,-1):
        #     far = min(n,i + nums[i] + 1)
        #     for j in range(i+1,far):
        #         dp[i] = min(dp[i],1 + dp[j])
        # return dp[0]
        #TC O(N)
        n = len(nums)
        jump = 0
        curr = 0
        farther = 0
        for i in range(n-1):
            farther = max(farther,nums[i]+i)
            if i == curr:
                jump+=1
                curr = farther
        return jump

            


        
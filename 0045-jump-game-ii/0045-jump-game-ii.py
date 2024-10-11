class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp = [float('inf')] * len(nums)
        # dp[0] = 0
        # for i in range(len(nums)):
        #     for j in range(0,i):
        #         if i <= j + nums[j]:
        #             dp[i] = min(dp[i],dp[j]+1)
        # return dp[-1]
        cur = 0
        far =nums[0]
        mid = 0
        for i in range(len(nums)-1):
            far = max(far,nums[i]+i)
            if far == len(nums)-1:
                mid +=1
                break
            if i == cur:
                cur = far
                mid +=1
        return mid


        
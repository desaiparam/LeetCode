class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        sumy = 0
        for i in range(len(nums)):
            sumy += nums[i]
            if sumy > maxi:
                maxi = sumy
            if sumy < 0:
                sumy = 0
        return maxi

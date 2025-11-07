class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxi = 0
        l = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                maxi = max(maxi,i-l+1)
                l = i+1
                print(nums[i],i,l)
        maxi = max(maxi, len(nums) - l)
        return maxi

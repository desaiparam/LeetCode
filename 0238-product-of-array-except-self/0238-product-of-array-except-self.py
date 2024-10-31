class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums)
        right = 1
        left[0] = 1
        ans = [0]*len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(len(nums)-1,-1,-1):
            ans[i] = left[i] * right
            right *= nums[i]
        return ans
        
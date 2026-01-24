class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        ans = 0
        while i <= j:
            val = nums[i]+nums[j]
            ans = max(ans,val)
            i += 1
            j -= 1
        return ans
        
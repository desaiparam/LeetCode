class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        ans = 0
        # for i in range(min(len(nums), ans + 1)):
        while i<len(nums) and i <= ans:
            ans = max(ans,min(i+nums[i],len(nums)-1))
            i += 1
        return ans==len(nums) -1
            
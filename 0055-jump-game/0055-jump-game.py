class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        for i in range(len(nums)):
            j = i + nums[i]
            if maxJump < i:
                return False
            maxJump = max(maxJump,j)
        return True

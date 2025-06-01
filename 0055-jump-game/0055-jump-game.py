class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        for i in range(0,len(nums)):
            print(i,"i")
            print(maxIndex,"maxIndex")
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex,i + nums[i])
        return True
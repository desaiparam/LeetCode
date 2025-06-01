class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        left = 0
        right = 0
        while (right < len(nums)-1):
            farthest = 0
            for i in range(left,right+1):
                farthest = max(i + nums[i],farthest)
            left = right + 1
            right = farthest
            jump += 1
        return jump

            
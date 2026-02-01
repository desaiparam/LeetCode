class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1 = float('inf')
        min2 = float('inf')
        for i in nums[1:]:
            if i < min1:
              min2 = min1
              min1 = i
            elif i < min2:
                min2 = i
        return nums[0] + min1+min2
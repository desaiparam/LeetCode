class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        for i in range(1,2**31-1):
            if i not in seen:
                return i


        
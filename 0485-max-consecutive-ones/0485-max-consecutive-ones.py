class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = c = 0
        for i in nums:
            if i == 1:
                c += 1
                m = max(m,c)
            elif i == 0:
                c = 0
        return m
        
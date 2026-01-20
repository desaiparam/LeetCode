class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i & 1:
                res.append(i & ~(((i+1) & ~i) >>1))
            else:
                res.append(-1)
        return res
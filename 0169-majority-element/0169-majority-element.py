class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sets ={}
        res = 0
        maj =0
        for i in nums:
            sets[i] = 1 + sets.get(i,0)
            if sets[i] > maj :
                res=i
                maj = sets[i]
        return res
        
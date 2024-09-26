class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set=set(nums)
        # print(nums)
        maxi  = -1
        num_neg = 0
        for i in range(len(nums)):
            if nums[i] > 0 and -nums[i] in num_set:
                maxi =  max(maxi,nums[i])
        return maxi

        
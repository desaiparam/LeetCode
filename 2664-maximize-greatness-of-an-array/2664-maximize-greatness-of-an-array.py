class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        prem = sorted(nums)
        i = 0
        j = 0
        count = 0
        while i < len(nums) and j < len(prem):
            if prem[j] > nums[i] :
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        return count
            


             
        
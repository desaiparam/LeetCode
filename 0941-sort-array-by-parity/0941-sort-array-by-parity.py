class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     if 
        i = 0
        j = 0
        while(j < len(nums)):
            if nums[j] % 2 == 0:
                nums[j],nums[i] = nums[i],nums[j]
                i += 1
            j += 1
        return nums
        
        
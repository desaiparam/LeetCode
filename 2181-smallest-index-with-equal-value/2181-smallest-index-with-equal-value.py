class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        #SOLUTION 1
        # smaller = min(nums)
        # for i in range(len(nums)):
        #     if i % 10 == nums[i] :
        #         print("nums[i]",nums[i])
        #         if(smaller<nums[i]):
        #             print("smaller",smaller)
        #             return i
        #         else:
        #             return i
        
        # return -1
        #SOLUTION 2
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1
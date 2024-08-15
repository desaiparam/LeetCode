class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        previous_element = nums[0]
        if len(nums) <= 1:
            print(nums)
            return
        i=1
        while i< len(nums):
            if nums[i]==previous_element:
                nums.pop(i)
                # previous_element = i
            else:
                previous_element = nums[i]
                i+=1
        print(nums)
        
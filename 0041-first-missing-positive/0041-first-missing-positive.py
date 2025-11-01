class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # TC O(N) SC O(N)
        seen = set(nums)
        for i in range(1,len(nums)+1):
            if i not in seen:
                return i
           
        return len(nums) + 1
            
         


        
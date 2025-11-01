class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # TC O(N) SC O(N)
        # seen = set(nums)
        # for i in range(1,len(nums)+1):
        #     if i not in seen:
        #         return i
           
        # return len(nums) + 1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = 0
        for i in range(n):
            change = abs(nums[i])
            if 1 <= change <= n:
                if nums[change-1] > 0:
                    nums[change-1] = -abs(nums[change-1])
                elif nums[change-1] == 0:
                    nums[change-1] = -1 * (n+1)
        for i in range(1,n+1):
            # print(nums)
            if nums[i-1] >= 0:
                return i
        return n +1
        # print(nums)
         


        
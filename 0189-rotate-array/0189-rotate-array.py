class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # n = len(nums) % k
        # print(n)
        new_nums = []
        # for i in range(k):
        #     # print(nums[n])
        #     # print(nums[-k:])
        #     # temp = nums[-k:]
        #     # print(temp)

        #     # nums.pop()
        #     # print(nums)
        if len(nums) < k :
            # nums[:] = nums[-n:] + nums[:-n]
            k = k % len(nums) 
        
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)
        # return new_nums
        """
        Do not return anything, modify nums in-place instead.
        """
        
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        pre_max = [0] * len(nums)
        suf_min = [0]* len(nums)
        pre_max[0]  = nums[0]
        # print(pre_max)
        for i in range(1,len(nums)):
            pre_max[i] = max(pre_max[i-1],nums[i])
            # print("pre_max",pre_max) 
        suf_min[len(nums)-1] = nums[len(nums) -1]
        # print(suf_min)
        for i in range(len(nums) -2 ,-1,-1):
            suf_min[i]= min(suf_min[i+1],nums[i])
            # print("suf_min",suf_min)
        total_sum = 0
        for i in range(1,len(nums)-1):
            if pre_max[i-1] < nums[i] < suf_min[i+1]:
                print(suf_min[i+1])
                total_sum += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                total_sum += 1
        return total_sum


       
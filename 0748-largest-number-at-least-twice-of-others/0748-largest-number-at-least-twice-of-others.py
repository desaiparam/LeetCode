class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = max(nums)
        # print(maxi)
        i = 0 
        count = 0
        while i < len(nums):
            if maxi >= 2 * nums[i] and nums[i] != maxi:
                print(2*nums[i],i)
                count += 1
                # return maxi
            i += 1
        if count == len(nums)-1:
            print("YSE")
            return nums.index(maxi)
        return -1
        
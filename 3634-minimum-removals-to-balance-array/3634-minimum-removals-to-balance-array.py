class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        maxy = 0
        for i in range(len(nums)):
            while nums[i]/nums[j] > k:
                j += 1
            if i -j  + 1 > maxy:
                maxy = i - j +1
        return len(nums) - maxy 
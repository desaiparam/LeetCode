class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        j = 0
        total = sum(nums)
        for i in range(len(nums)-1):
            j += nums[i]
            newr = total - j
            if (j - newr) % 2 == 0:
                count += 1
        return count
            


        
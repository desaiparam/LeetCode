class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0
        lastSmaller = float('-inf')
        current = 1
        for i in range(len(nums)):
            if nums[i]- 1 == lastSmaller:
                current += 1
                lastSmaller = nums[i]
            elif nums[i] != lastSmaller:
                current = 1
                lastSmaller = nums[i]
            longest = max(current,longest)
        return longest
        
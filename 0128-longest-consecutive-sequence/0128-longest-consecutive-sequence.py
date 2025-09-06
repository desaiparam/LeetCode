class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for i in seen:
            if i - 1 not in seen:
                count = 1
                curr = i
                while curr + 1 in seen:
                    curr += 1
                    count += 1
                longest = max(longest,count)
        return longest


            


        
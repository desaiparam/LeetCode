class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # left = 0
        # right = len(nums) -1
        # while left < right:
        #     # target = nums[left]
        #     mid = (left + right)//2
        #     target = sum(1 for i in nums if i <= mid)
        #     if mid < target:
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left
        seen = set()
        for i in nums:
            if i in seen:
                return i
            else:
                seen.add(i)

        
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def helper(dist):
            lefty = 0
            res = 0
            for righty in range(len(nums)):
                while nums[righty] - nums[lefty] > dist:
                    lefty += 1
                res += righty - lefty
            return res
        left = 0
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            p = helper(mid)
            if p >= k:
                right = mid
            else:
                left = mid + 1
        return left

        
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def most(k):
            if k < 0:
                return 0
            l = 0
            r = 0
            sumy = 0
            count = 0
            while r < len(nums):
                sumy += nums[r] % 2
                while sumy > k:
                    sumy -= nums[l] % 2
                    l += 1
                count += r-l+1
                r += 1
            return count
        return most(k) - most(k- 1)

        
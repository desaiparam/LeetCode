class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        def helper(maxsum):
            split = 1
            sumy = 0
            for i in nums:
                if sumy+i > maxsum:
                    split += 1
                    sumy = i
                else:
                    sumy += i
            print(sumy)
            return split
        while low <= high:
            mid = low + (high - low) //2
            maxsumy = helper(mid)
            if maxsumy<=k:
                high = mid - 1
            else:
                low = mid + 1
        return low
        
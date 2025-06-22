class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        # sumy = 0
        ans = -1
        while  low <= high:
            mid = (low + high) //2
            sumy = sum(math.ceil(i / mid) for i in nums)
            if sumy <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return low
        
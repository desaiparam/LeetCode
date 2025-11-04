class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        for i in nums:
            low = 0
            high = len(res)
            while low < high:
                mid = low + (high - low) // 2
                if res[mid] >= i:
                    high = mid
                else:
                    low = mid + 1
            if len(res) == low:
                res.append(i)
            else:
                res[low] = i
        return len(res) 

        
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)-k+1):
            j = i+k-1
            ans = min(ans,nums[j]-nums[i])
        return ans
        
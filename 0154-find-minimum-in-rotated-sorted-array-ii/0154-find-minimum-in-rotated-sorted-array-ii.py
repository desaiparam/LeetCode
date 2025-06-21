class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums) -1
        ans = float('inf')
        while low <= high:
            mid = (low+high) // 2
            ans = min(ans,nums[low])
            if nums[mid] == nums[low] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            if nums[mid] >= nums[low]:
                ans = min(ans,nums[low])
                low = mid + 1
            else:
                ans = min(ans,nums[mid])
                high = mid - 1
        return ans
             

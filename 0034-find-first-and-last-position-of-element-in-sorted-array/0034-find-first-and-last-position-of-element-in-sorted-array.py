class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) -1
        ans = []
        while left <= right:
            mid = left + (right - left) //2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        ans.append(left)
        left2 = left
        right2 = len(nums) - 1
        while left2 <= right2:
            mid2 = left2 + ((right2 - left2) // 2)
            if nums[mid2] <= target:
                left2 = mid2 + 1
                
            else:
                right2 = mid2 - 1
        ans.append(right2)
        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        return ans
        
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #TC O(N) SC O(N)
        # freq = Counter(nums)
        # for i in nums:
        #     if freq[i] == 1:
        #         return i
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[-1]
        if nums[0] != nums[1]:
            return nums[0]
        low = 1
        high = n-2
        while low <= high:
            mid = (low + high)//2
            print(mid,low)
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1]):
                low = mid + 1
            else:
                high = mid -1
        # return low
    
        
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def most(k):
            if k < 0 :
                return 0
            l = 0
            r = 0
            sumy = 0
            count = 0
            while r < len(nums):
                sumy += nums[r]
                while sumy > k:
                    sumy -= nums[l]
                    l += 1
                count += r-l+1
                r+=1
            return count
        return most(goal) - most(goal-1)
            
        
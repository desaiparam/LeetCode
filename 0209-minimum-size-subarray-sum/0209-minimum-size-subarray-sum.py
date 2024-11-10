class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left =  curr = 0
        ans = float('inf')
        for right in range(len(nums)):
            curr += nums[right]
            print(curr)
            while curr >= target:
                ans = min(ans,right - left + 1)
                print(curr)
                curr -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans

        
           
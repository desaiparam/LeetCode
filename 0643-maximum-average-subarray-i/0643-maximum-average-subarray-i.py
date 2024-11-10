class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = ans = sum(nums[:k])
        print(curr)
        for right in range(k,len(nums)):
            curr += nums[right] - nums[right-k]
            print(curr)

            # while curr > k:
            #     curr -= nums[left]
            #     left += 1
            ans=max(curr,ans)
        
        return ans/k
        
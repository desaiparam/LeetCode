class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7 
        leftmap = {}
        rightmap = {}
        for i in nums:
            rightmap[i] = rightmap.get(i,0) + 1
        ans = 0
        for j in range(len(nums)):
            rightmap[nums[j]] -= 1
            i = nums[j]*2
            ans += leftmap.get(i,0) * rightmap.get(i,0) 
            ans %= MOD
            leftmap[nums[j]] = leftmap.get(nums[j],0) + 1
        return ans

           
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        maxi = 0
        ans = 0
        for i in nums:
            if maxi < hashmap[i]:
                maxi = hashmap[i]
                ans = i
        print(hashmap)
        return ans       
        
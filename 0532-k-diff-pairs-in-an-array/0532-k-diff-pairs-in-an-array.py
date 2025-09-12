class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        seen = set()
        i = 0
        j =  1
        while i < len(nums) and j < len(nums):
            if i == j or abs(nums[i] - nums[j]) < k:
                print("j",abs(nums[i] - nums[j]))
                j += 1
            elif abs(nums[i] - nums[j]) > k:
                print("i",abs(nums[i] - nums[j]))
                i += 1
            else:
                seen.add((nums[i] ,nums[j]))
                i += 1
                j += 1
        print(seen)
        return len(seen)
        
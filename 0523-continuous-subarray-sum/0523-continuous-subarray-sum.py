class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        hashmap = {0:-1}
        rsum = 0
        for i in range(len(nums)):
            rsum += nums[i]
            left = rsum % k
            if left not in hashmap:
                hashmap[left] = i
            else:
                if i - hashmap[left] >= 2:
                    return True
        return False

        
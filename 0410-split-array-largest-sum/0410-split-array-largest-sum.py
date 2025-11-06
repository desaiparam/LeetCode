class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #TC O(log(sum(n)-max(n)).n) SC O(1)
        # The concept over here is that the k is we will check the splits with maxsum possible from the array of max in the nums array and the total sum. This is the range of the array we will do bs and then find the possible sum which has the best value
        low = max(nums)
        high = sum(nums)
        def helper(maxsum):
            split = 1
            sumy = 0
            for i in nums:
                if sumy+i > maxsum:
                    split += 1
                    sumy = i
                else:
                    sumy += i
            return split
        while low <= high:
            mid = low + (high - low) //2
            maxsumy = helper(mid)
            if maxsumy <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low
        
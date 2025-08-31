class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        ans = 0
        left = 0
        pairs = 0
        for right in range(len(nums)):
            curr = nums[right]
            pairs += freq[curr]
            freq[curr] += 1
            while pairs >= k:
                ans += (len(nums) - right)
                i = nums[left]
                freq[i] -= 1
                pairs -= freq[i]
                left += 1
        return ans
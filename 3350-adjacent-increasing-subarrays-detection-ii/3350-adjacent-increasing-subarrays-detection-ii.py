class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Step 1: incLen[i] = length of increasing sequence starting at i
        incLen = [1] * n

        # Fill from right to left
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                incLen[i] = incLen[i + 1] + 1

        max_k = 0

        # Step 2: Try each starting index
        for start in range(n):
            first_len = incLen[start]
            second_start = start + first_len

            if second_start < n:
                second_len = incLen[second_start]
                possible_k = min(first_len, second_len)
                max_k = max(max_k, possible_k)

        max_k = max(max_k, int(max(incLen) / 2))

        return max_k
            
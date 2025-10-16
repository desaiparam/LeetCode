class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.memo = [-1] * len(arr)
        def helper(idx):
            if idx >= len(arr):
                return 0
            if self.memo[idx] != -1:
                return self.memo[idx]
            currSum = 0
            maxSum = 0
            for i in range(1,k+1):
                if idx + i > len(arr):
                    break
                currSum = max(currSum,arr[idx + i - 1])
                currMax = currSum*i + helper(i+idx)
                # print(currSum,currMax)
                maxSum = max(maxSum,currMax)
            self.memo[idx] = maxSum
            return maxSum
        return helper(0)
            
        
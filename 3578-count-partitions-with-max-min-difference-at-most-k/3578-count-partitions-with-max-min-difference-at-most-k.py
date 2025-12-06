class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # MOD = 10 ** 9 + 7
        # memo = {}
        # def dfs(i):
        #     if i >= len(nums):
        #         return 1
        #     count = 0
        #     maxi = nums[i]
        #     mini = nums[i]
        #     if i in memo:
        #         return memo[i]
        #     for j in range(i,len(nums)):
        #         maxi = max(maxi,nums[j])
        #         mini = min(mini,nums[j])
        #         if maxi - mini <= k:
        #             count = (count + dfs(j+1)) % MOD
        #         else:
        #             break
        #     memo[i] = count
        #     return count
        # return dfs(0) 
        MOD = 10 ** 9 + 7
        n = len(nums) 
        dp = [0] * (n+1)
        prefix = [0] * (n+2)
        dp[0] = 1
        prefix[1] = 1
        maxi = deque()
        mini = deque()
        l = 0
        for r in range(n):
            while maxi and nums[maxi[-1]] <= nums[r]:
                maxi.pop()
            maxi.append(r)
            while mini and nums[mini[-1]] >= nums[r]:
                mini.pop()
            mini.append(r)
            while nums[maxi[0]] - nums[mini[0]] > k:
                if maxi[0] == l:
                    maxi.popleft()
                if mini[0] == l:
                    mini.popleft()
                l += 1
            dp[r+1] = (prefix[r+1] - prefix[l]) % MOD
            prefix[r+2] = (prefix[r+1] + dp[r+1]) % MOD
        return dp[n]

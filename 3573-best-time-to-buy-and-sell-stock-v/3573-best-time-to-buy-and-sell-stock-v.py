class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # can not use recurrsion as way to much space overhead as stack and memo both takes a lot of space
        # n = len(prices)
        # memo = {}
        # def helper(idx,trans,canbuy):
        #     key = (trans, canbuy)
        #     if trans == k or idx == n:
        #         if canbuy == 1:
        #             return 0
        #         else:
        #             return float('-inf')
        #     if key in memo:
        #         return memo[key]
        #     if canbuy == 1: #flat
        #         lon =  -prices[idx]+ helper(idx+1,trans,-1)
        #         short = prices[idx] + helper(idx+1,trans,0)
        #         skip = helper(idx+1, trans, 1)
        #         profit = max(lon,skip,short)
        #     elif canbuy == -1: # long
        #         lon = prices[idx] + helper(idx+1,trans+1,1)
        #         skip = helper(idx+1, trans, -1)
        #         profit = max(lon,skip)
        #     elif canbuy == 0:#short
        #         close = -prices[idx] + helper(idx+1,trans+1,1)
        #         skip = helper(idx+1, trans, 0)
        #         profit = max(skip,close)
        #     memo[key] = profit
        #     return profit
        # return helper(0,0,1)
        
        n = len(prices)
        dp = [[float('-inf')]*3 for _ in range(k+1)]
        dp[0][0] = 0
        for p in prices:
            newdp = [[float('-inf')]*3 for _ in range(k+1)]
            for t in range(k+1):
                newdp[t][0] = max(newdp[t][0],dp[t][0])
                if t >0:
                    newdp[t][0] = max(newdp[t][0],dp[t-1][1]+p)
                if t >0:
                    newdp[t][0] = max(newdp[t][0],dp[t-1][2]-p)
                newdp[t][1] = max(newdp[t][1],dp[t][1])
                newdp[t][1] = max(newdp[t][1],dp[t][0] - p)
                newdp[t][2] = max(newdp[t][2],dp[t][2])
                newdp[t][2] = max(newdp[t][2],dp[t][0] + p)
            dp = newdp
        return max(dp[t][0] for t in range(k + 1))




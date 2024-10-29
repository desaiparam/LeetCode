class Solution:
    #SOLUTION 1
    # def pr(self,idx:int,b:int,val:int,n:int,dp:List[List[int]]):
    #     if idx==n: 
    #         return 0
    #     if dp[idx][b] != -1:
    #         return dp[idx][b]
    #     if b:
    #         profit = max(-val[idx]+self.pr(idx+1,0,val,n,dp),0+self.pr(idx+1,1,val,n,dp))
    #     else:
    #         profit = max(val[idx]+self.pr(idx+1,1,val,n,dp),0+self.pr(idx+1,0,val,n,dp))
    #     dp[idx][b] = profit
    #     return dp[idx][b]

    def maxProfit(self, prices: List[int]) -> int:
        #SOLUTION 1
        # dp = [[-1] * 2 for _ in range(len(prices))]
        # return self.pr(0,1,prices,len(prices),dp)
        n=len(prices)
        #SOLUTION 2
        dp = [[0] * 2 for _ in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        for idx in range(n-1,-1,-1):
            print(idx)
            for b in range(2):
                if b:
                    profit = max(-prices[idx]+dp[idx+1][0],0+dp[idx+1][1])
                else:
                    profit = max(prices[idx]+dp[idx+1][1],0+dp[idx+1][0])
                dp[idx][b] = profit
        return dp[0][1]
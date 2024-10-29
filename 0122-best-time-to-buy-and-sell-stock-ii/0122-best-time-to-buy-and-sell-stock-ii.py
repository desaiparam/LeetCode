class Solution:
    def pr(self,idx:int,b:int,val:int,n:int,dp:List[List[int]]):
        if idx==n: 
            return 0
        if dp[idx][b] != -1:
            return dp[idx][b]
        if b:
            profit = max(-val[idx]+self.pr(idx+1,0,val,n,dp),0+self.pr(idx+1,1,val,n,dp))
        else:
            profit = max(val[idx]+self.pr(idx+1,1,val,n,dp),0+self.pr(idx+1,0,val,n,dp))
        dp[idx][b] = profit
        return dp[idx][b]

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 2 for _ in range(len(prices))]
        return self.pr(0,1,prices,len(prices),dp)
        
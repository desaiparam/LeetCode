class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mini = prices[0]
        # profit = 0
        # for i in range(1,len(prices)):
        #     cost = prices[i] - mini
        #     profit = max(profit,cost)
        #     mini = min(mini,prices[i])
        # return profit
        min_price = prices[0]
        # print(min_price)
        profit = 0
        for i in range(1,len(prices)):
            profit = max(profit,prices[i] - min_price)
            min_price = min(min_price,prices[i])
        return profit
            # profit = max(profit,cost)
        
        
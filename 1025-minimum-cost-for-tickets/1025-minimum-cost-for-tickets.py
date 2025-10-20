class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        onepass = costs[0]
        sevenpass = costs[1]
        monthpass = costs[2]
        durations = [1,7,30]
        dp = [-1]*len(days)
        def helper(idx):
            if idx >= len(days):
                return 0
            if dp[idx] != -1:
                return dp[idx]
            miny = float('inf')
            for cost, duration in zip(costs, durations):
                next_idx = idx
                while next_idx < len(days) and days[next_idx] <= days[idx] + duration - 1:
                    next_idx += 1
                totalcost = cost+helper(next_idx)
                miny = min(totalcost,miny)
            dp[idx] = miny
            return dp[idx]
        return helper(0)

        

        
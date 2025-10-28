class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #TLE
        # num =1
        # count = 0
        # memo = {}
        # def isUgly(x):
        #     if x in memo:
        #         return memo[x]
        #     og = x
        #     for mul in [2,3,5]:
        #         while x % mul == 0:
        #             x //=mul
        #     memo[og] = (x == 1)
        #     return memo[og]
        # while True:
        #     if isUgly(num):
        #         count += 1
        #         if count == n:
        #             return num
        #     num += 1
        seen = set()
        minheap =[1]
        for i in range(n):
            nums = heapq.heappop(minheap)
            if i == n-1:
                return nums
            for mul in [2,3,5]:
                val = mul * nums
                if val not in seen:
                    seen.add(val)
                    heapq.heappush(minheap,val)


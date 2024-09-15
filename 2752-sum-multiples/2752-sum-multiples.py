class Solution:
    def sumOfMultiples(self, n: int) -> int:
        #SOLUTION 1
        # return sum([i for i in range(1,n+1) if i % 3 ==0 or i % 5 ==0 or i % 7 ==0 ])
        # SOLUTION 2
        def sum(k):
            j = n//k
            return j * k * (j+1)//2
        ans = sum(3) + sum(5) + sum(7) + sum(105) - sum(15) - sum(21) - sum(35)
        return ans
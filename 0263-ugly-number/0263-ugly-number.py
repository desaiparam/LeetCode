class Solution:
    def isUgly(self, n: int) -> bool:
        #TC and SC O(logn)
        # def helper(n):
        #     if n <= 0:
        #         return False
        #     if n == 1:
        #         return True
        #     if n % 2 == 0:
        #         return helper(n//2)
        #     if n % 3 == 0:
        #         return helper(n//3)
        #     if n % 5 == 0:
        #         return helper(n//5)
        #     return False
        # return helper(n)
        #TC O(N) SC O(1)
        if n <= 0 :
            return False
        for mul in [2,3,5]:
            while n % mul == 0:
                n //= mul
        return n == 1
        
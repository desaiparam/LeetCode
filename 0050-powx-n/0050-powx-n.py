class Solution:
    def myPow(self, x: float, n: int) -> float:
        newX = abs(n)
        res = 1
        while newX != 0:
            if newX %2 == 1:
                res *= x
            x *= x
            newX //= 2
        return res if n > 0 else 1/res
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 0
        if n == 0:
            return 1
        power = self.myPow(x,abs(n)//2)
        ans = power*power
        if abs(n) % 2 == 1:
            ans *= x
        return ans if n>0 else 1/ans
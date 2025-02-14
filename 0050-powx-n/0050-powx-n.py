class Solution:
    def myPow(self, x: float, n: int) -> float:
        # def help(x,n):
        #     if n == 0:
        #         return 1

        #     h = help(x,abs(n)//2)
        #     res = h * h
        #     if abs(n) % 2 == 1:
        #         res *= x
        #     return res if n > 0 else 1/res
        
        
        # return help(x,n)
        res = 0
        if n == 0:
            return 1
        
        h = self.myPow(x,abs(n)//2)
        res = h * h
        print(res)
        if abs(n) % 2 == 1:
            res *= x
        return res if n > 0 else 1/res
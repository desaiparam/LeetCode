class Solution:
    def myPow(self, x: float, n: int) -> float:
        # newN = n
        # newX = 1
        # if newN < 0:
        #     while newN < 0:
        #         # print(newN)
        #         newX = newX * x
        #         newN += 1
        #         # print(newX)
        #     newX = 1 / newX
        # else:     
        #     while newN > 0:
        #         # print(newN)
        #         newX = newX * x 
        #         # print(newX)
        #         newN -= 1
        ans = 0
        def help(x,n):
            # newX = 1
            if n == 0:
                return 1

            h = help(x,abs(n)//2)
            res = h * h
            if abs(n) % 2 == 1:
                res *= x
            return res if n > 0 else 1/res
        
        
        return help(x,n)
        # return x**n
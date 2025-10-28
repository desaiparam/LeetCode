class Solution:
    def reverse(self, x: int) -> int:
        #TC and SC O(N)
        # newX = str(x)
        # res = ""
        # if x < 0:
        #     res += "-"
        
        # for i in range(len(newX)-1,-1,-1):
        #     if newX[i] != "-":
        #         res+= newX[i]
        # return int(res) if -2147483648<=int(res)<=2147483647  else 0
        #TC O(N) SC O(1)
        res = 0
        newX=abs(x)
        while newX != 0:
            digit = newX % 10
            res = res*10 + digit
            newX //= 10
        if x < 0:
            res *= -1
        return res if -2**31<= res <= 2**31 else 0
        



        
        
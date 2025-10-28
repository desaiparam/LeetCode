class Solution:
    def reverse(self, x: int) -> int:
        newX = str(x)
        res = ""
        if x < 0:
            res += "-"
        
        for i in range(len(newX)-1,-1,-1):
            if newX[i] != "-":
                res+= newX[i]
        return int(res) if -2147483648<=int(res)<=2147483647  else 0

        
        
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
       x = n ^ (n >> 1)
       print(x)
       return  (x & x + 1) == 0
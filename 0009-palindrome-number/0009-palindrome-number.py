class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        newX = abs(x)
        res = 0
        while newX != 0:
            digit = newX % 10
            res = res * 10 + digit
            newX //= 10
        return res == x
        
            
        
class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        carry = 0
        while n > 0:
            
            if n % 2 == 1:
                if( n & 2) == 0:
                    count += 1
                else:
                    carry = 1
                    count += 1
            else:
                carry = 0
            n = (n + carry) // 2
        return count
            

        
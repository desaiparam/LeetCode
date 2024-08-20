class Solution:
    def reverse(self, x: int) -> int:
       
        new_i = []
        reve =0
        if x < 0:
            new_i.append('-') 
            x = abs(x) 
        reve = int(''.join(reversed(str(x))))
        if '-' in new_i:
            reve = -reve
        if reve >2**31-1 or reve<-(2**31):
            return 0
        
        return reve
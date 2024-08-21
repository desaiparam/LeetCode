import re
class Solution:
    def myAtoi(self, s: str) -> int:
        num = '[0-9]'
        new_s= ''
        new_i = 0
        for char in s:
            if char == ' ' and len(new_s) ==0:
                continue
            if char!= ' ' and (char in '-+' or re.match(num,char) ) and len(new_s) ==0:
                new_s +=char
            elif re.match(num,char):
                new_s+=char
            else:
                break
        if new_s == ' ' or new_s in '-+':
            return 0
        else:
            new_i = int(new_s)
            if  new_i>2**31-1:
                return 2**31-1
            elif  new_i<-(2**31):
                return -(2**31)
        return new_i
        
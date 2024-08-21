import re
class Solution:
    def myAtoi(self, s: str) -> int:
        pattern ='[a-zA-Z.]'
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

        # if len(s) == 0:
        #     return 0
        # elif re.match(pattern, s[0]):
        #     return 0
        # else:
        #     for i,char in enumerate(s) :
        #         # print("out",char)
        #         if " " not in  char :
        #             # print("btw",char)
        #             if re.match(pattern, char):
        #                 break
        #             elif  re.match(num,char):
        #                 # print("in",char)
        #                 new_s+=char
        #         if '-' in char:
        #             if i > 0 and s[i - 1] == ' ':
        #                 new_s+='-'+new_s
        #             elif s[i]=="-" and i==0:
        #                 if s[i+1] =="+":
        #                     return 0
        #                 else:
        #                     new_s+='-'+new_s
        #             else :
        #                 return 0
        # print(new_s)
        
        # if new_s:
        #     new_i = int(new_s)
        #     print(new_i)

        # if  new_i>2**31-1 or new_i<-(2**31):
        #     return -(2**31)
        
        return new_i
        
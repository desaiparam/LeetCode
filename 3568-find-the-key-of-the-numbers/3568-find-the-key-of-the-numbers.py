class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        lis = [0]*4
        i =0
        while num1 != 0 or num2 != 0 or num3 != 0 :
            mi = min(num1%10,num2%10,num3%10)
            num1 = num1//10
            num2 = num2//10
            num3 = num3//10
            lis[i] +=mi
            i+=1
        re=0
        for j in range(3,-1,-1):
            re = re *10 + lis[j] 

        return re
class Solution:
    def addDigits(self, num: int) -> int:
        # newN = num
        # count  = 0
        # # while len(num) != 1:
        #     result += newN % 10 
        #     newN //= 10
        #     count += 1
        # return count
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return (num % 9)
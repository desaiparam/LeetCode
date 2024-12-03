class Solution:
    def isUgly(self, n: int) -> bool:
        newN = n
        if n <= 0:
            return False
        # print(newN)
        while newN > 1:
            if newN % 3 == 0:
                print(newN/3)
                newN //= 3
            elif newN % 2 == 0:
                newN //= 2
            elif newN % 5 == 0:
                newN //= 5
            else:
                return False
        # print(newN)
        return True
class Solution:
    def numberCount(self, a: int, b: int) -> int:
        count = 0
        for i in range(a,b+1):
            newS = str(i)
            if len(set(newS)) == len(newS):
                count += 1
        return count

        
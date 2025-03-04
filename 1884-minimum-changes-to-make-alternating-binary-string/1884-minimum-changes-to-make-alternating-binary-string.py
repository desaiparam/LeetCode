class Solution:
    def minOperations(self, s: str) -> int:
        change = 0
        for i , c in enumerate(s):
            print(c)
            print("i",i%2)
            if int(c) == i % 2:
                change += 1
                print("change",change)
        return min(change,len(s) - change)
       
        
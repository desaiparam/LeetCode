class Solution:
    def scoreOfString(self, s: str) -> int:
        sumy = 0
        for i in range(len(s)-1):
            sumy += abs(ord(s[i])-ord(s[i+1]))
            print(sumy)

        return sumy
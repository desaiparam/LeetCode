class Solution:
    def getSmallestString(self, s: str) -> str:
        chars = list(s)
        for i in range(len(s)-1):
            if int(s[i]) > int(s[i+1]):
                if int(s[i]) % 2 == int(s[i+1]) % 2: 
                    chars[i] , chars[i+1] = chars[i+1] , chars[i]
                    break
        return ''.join(chars)
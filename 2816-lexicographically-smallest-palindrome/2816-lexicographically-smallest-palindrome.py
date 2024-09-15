class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        i=0
        j=len(s)-1
        newS = ""
        while i<=j:
            # print("i",i)
            # print("j",j)
            if s[i] != s[j]:
                if ord(s[i])-ord('a') <ord(s[j])-ord('a'):
                    # print(s)
                    s[j] = s[i]
                else:
                    s[i] = s[j]
                    # print(s)
            i+=1
            j-=1
        s = ''.join(s)
        return s
        
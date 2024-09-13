class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber>0:
            columnNumber-=1
            cur = chr((columnNumber%26)+ord('A'))
            ans=cur+ans
            columnNumber//=26
        return ans

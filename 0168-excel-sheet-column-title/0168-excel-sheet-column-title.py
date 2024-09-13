class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = list(string.ascii_uppercase)
        temp=[]
        while columnNumber>0:
            columnNumber-=1
            temp.append(a[(columnNumber%26)]) 
            columnNumber//=26
        temp.reverse()
        return "".join(temp)

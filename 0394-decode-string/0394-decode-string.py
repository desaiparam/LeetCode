class Solution:
    def decodeString(self, s: str) -> str:
        numSt = []
        strSt = []
        currNum = 0
        curStr = []
        for i in  range(len(s)):
            c = s[i]
            if c.isdigit():
                currNum = currNum*10 + int(c)
            elif c == "[":
                strSt.append(curStr)
                numSt.append(currNum)
                currNum = 0
                curStr = []
            elif c == "]":
                pnt = strSt.pop()
                cnt = numSt.pop()
                curStr = pnt + curStr * cnt 
            else:
                curStr.append(c)
        return ''.join(curStr)
            


        
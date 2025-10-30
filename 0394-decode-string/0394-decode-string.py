class Solution:
    def decodeString(self, s: str) -> str:
        intStack = []
        charStack = []
        res = ""
        currNum = 0
        for i in range(len(s)):
            curr = s[i]
            if curr.isdigit():
                currNum = currNum * 10 + int(curr)
            elif curr == "[":
                charStack.append(res)
                intStack.append(currNum)
                currNum = 0
                res = ""
            elif curr == "]":
                inti = intStack.pop()
                char = charStack.pop()
                res = char + res * inti
                #  += newS
            else:
                res+=curr
        return res


        
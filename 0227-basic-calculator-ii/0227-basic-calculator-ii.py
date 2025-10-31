class Solution:
    def calculate(self, s: str) -> int:
        currNum = 0
        stack = []
        operations = {"+","-","*","/"}
        lastOp = '+'
        for i in range(len(s)):
            curr = s[i]
            if curr.isdigit():
                currNum = currNum * 10 + int(curr)
            # print(currNum)
            if curr in operations or i == len(s)- 1:
                if lastOp == '*':
                    stack.append(stack.pop()*currNum)
                elif lastOp == '/':
                    print("gweg")
                    stack.append(int(stack.pop()/currNum))
                elif lastOp == '+':
                    stack.append(currNum)
                elif lastOp == '-':
                    stack.append(-currNum)
                lastOp = curr 
                currNum = 0
            
            # print(stack)
        return sum(stack)
     
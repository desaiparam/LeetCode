class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        currNum = 0
        lastsign = '+'
        calc = 0
        for i in range(n):
            curr = s[i]
            if curr.isdigit():
                currNum = currNum * 10 + int(curr)
            elif curr == "(":
                # print(stack)
                if lastsign == '+':
                    stack.append(float('inf'))
                else:
                    stack.append(float('-inf'))
                lastsign = '+'
                currNum = 0
            elif curr == ")":
                if lastsign == '-':
                    stack.append(-currNum) 
                else:
                    stack.append(currNum)
                inter = 0
                while stack and stack[-1] not in  (float('inf'),float('-inf')):
                    inter += stack.pop()
                poped = stack.pop()
                if  poped == float('inf'):
                    stack.append(inter)
                else:
                    stack.append(-inter)
                currNum = 0
            elif not curr.isdigit() and curr != ' ':
                if lastsign == "-":
                    stack.append(-currNum) 
                else:
                    stack.append(currNum)
                lastsign = curr
                currNum = 0
        if s[n-1] != ")":
            if lastsign == '+':
                stack.append(currNum)
            else:
                stack.append(-currNum)

        print(stack)
        while stack:
            calc += stack.pop()
        return calc


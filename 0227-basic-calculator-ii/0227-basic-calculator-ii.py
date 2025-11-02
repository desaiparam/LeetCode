class Solution:
    def calculate(self, s: str) -> int:
        #TC O(N) SC O(N)
        # currNum = 0
        # stack = []
        # operations = {"+","-","*","/"}
        # lastOp = '+'
        # for i in range(len(s)):
        #     curr = s[i]
        #     if curr.isdigit():
        #         currNum = currNum * 10 + int(curr)
        #     if curr in operations or i == len(s)- 1:
        #         if lastOp == '*':
        #             stack.append(stack.pop()*currNum)
        #         elif lastOp == '/':
        #             stack.append(int(stack.pop()/currNum))
        #         elif lastOp == '+':
        #             stack.append(currNum)
        #         elif lastOp == '-':
        #             stack.append(-currNum)
        #         lastOp = curr 
        #         currNum = 0
        # return sum(stack)
        #TC O(N) SC O(1)
        tail = 0
        calc = 0
        lastsign = '+'
        currNum = 0
        for i in range(len(s)):
            curr = s[i]
            if curr.isdigit():
                currNum = currNum * 10 + int(curr)
            if (not curr.isdigit() and curr != ' ') or i == len(s) -1:
                if lastsign == '+':
                    calc += currNum
                    tail = currNum
                elif lastsign == '-':
                    calc -= currNum
                    tail = -currNum
                elif lastsign == '*':
                    calc = (calc - tail) + int(tail * currNum )
                    tail = tail*currNum
                elif lastsign == '/':
                    calc = (calc - tail) + int(tail/currNum)
                    tail = int(tail/currNum)
                lastsign = curr
                currNum = 0
        return calc

     
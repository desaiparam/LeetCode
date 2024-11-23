class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+', '-', '*','/'}
        for i in tokens:
            stack.append(i)
            if i in op:
                if len(stack) >= 3:
                    oper = stack.pop()
                    f_v = int(stack.pop())
                    s_v = int(stack.pop())
                    if oper == '+':
                        result = f_v + s_v
                        stack.append(result)
                    if oper == '-':
                        result = s_v - f_v
                        stack.append(result)
                    if oper == '*':
                        result = f_v * s_v
                        stack.append(result)
                    if oper == '/':
                        result = s_v / f_v
                        stack.append(result)
        return int(stack[-1])


        

        
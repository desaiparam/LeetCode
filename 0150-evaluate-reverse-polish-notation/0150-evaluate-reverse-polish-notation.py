class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+', '-', '*','/'}
        for i in tokens:
            # stack.append(i)
            if i in op:
                # if len(stack) >= 3:
                    # i = stack.pop()
                f_v = int(stack.pop())
                s_v = int(stack.pop())
                if i == '+':
                    result = f_v + s_v
                    # stack.append(result)
                elif i == '-':
                    result = s_v - f_v
                    # stack.append(result)
                elif i == '*':
                    result = f_v * s_v
                    # stack.append(result)
                elif i == '/':
                    result = s_v / f_v
                stack.append(result)
            else:
                stack.append(i)
        return int(stack[-1])


        

        
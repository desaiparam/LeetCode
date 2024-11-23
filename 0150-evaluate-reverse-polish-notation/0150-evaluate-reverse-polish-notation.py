class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # print(((10 * (6 / ((9 + 3) * -11))) + 17) + 5)
        stack = []
        op = {'+', '-', '*','/'}
        for i in tokens:
            # if i not in op:

            stack.append(i)
            if i in op:
                if len(stack) >= 3:
                    oper = stack.pop()
                    f_v = int(stack.pop())
                    s_v = int(stack.pop())
                    # print(f_v,s_v)
                    if oper == '+':
                        result = f_v + s_v
                        # print(result)
                        stack.append(result)
                    if oper == '-':
                        result = s_v - f_v
                        # print(result)
                        stack.append(result)
                    if oper == '*':
                        result = f_v * s_v
                        # print(result)
                        stack.append(result)
                    if oper == '/':
                        result = s_v / f_v
                        # print(result)
                        # if result < 0:
                        #     result = 0
                        # print("result",result)
                        stack.append(result)
                    # print(stack)
                else:
                    print("Not enough items in the stack to pop two values.")
                    # print(i)
            ans = int(stack[-1])
        # print(stack)
        # return stack[-1]
        return ans


        

        
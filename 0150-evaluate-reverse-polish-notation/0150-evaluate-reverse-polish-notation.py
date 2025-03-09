class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # operations = {'+','-','*','/'}
        for i in tokens:
            # stack.append(i)
            # print(stack)
            # if i in operations:
            # operator = stack.pop()
            # first_pop = int(stack.pop())
            # second_pop = int(stack.pop())
            if i == '+':
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif i == '-':
                a,b =  stack.pop() , stack.pop() 
                stack.append(b-a)
            elif i == '*':
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif i == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return int(stack[0])

        # for c in tokens:
        #     if c == '+':
        #         stack.append(stack.pop() + stack.pop())
        #     elif c == '-':
        #         a, b = stack.pop(), stack.pop()
        #         stack.append(b - a)
        #     elif c == '*':
        #         stack.append(stack.pop() * stack.pop())
        #     elif c == '/':
        #         a, b = stack.pop(), stack.pop()
        #         stack.append(int(b / a))     
        #     else:
        #         stack.append(int(c))
        # return stack[0]
            
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+','-','*','/'}
        for i in tokens:
            stack.append(i)
            # print(stack)
            if i in operations:
                operator = stack.pop()
                first_pop = int(stack.pop())
                second_pop = int(stack.pop())
                if operator == '+':
                    result = first_pop + second_pop
                    stack.append(result)
                if operator == '-':
                    result = second_pop - first_pop 
                    stack.append(result)
                if operator == '*':
                    result = first_pop * second_pop
                    stack.append(result)
                if operator == '/':
                    result = second_pop / first_pop
                    stack.append(result)
        return int(stack[-1])

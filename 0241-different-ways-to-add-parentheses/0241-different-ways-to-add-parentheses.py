class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        def helper(exp):
            res = []
            if exp.isdigit():
                return [int(exp)]
            for i in range(len(exp)):
                if exp[i] in "+-*":
                    left = helper(exp[:i])
                    right = helper(exp[i+1:])
                    for l in left:
                        for r in right:
                            if exp[i] == "*":
                                res.append(l * r)
                            if exp[i] == "-":
                                res.append(l - r)
                            if exp[i] == "+":
                                res.append(l + r)
            return res
       
        return  helper(expression)
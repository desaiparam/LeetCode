class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        #TC and SC O(N*2^N)
        # n = len(expression)
        # def helper(exp):
        #     res = []
        #     if exp.isdigit():
        #         return [int(exp)]
        #     for i in range(len(exp)):
        #         if exp[i] in "+-*":
        #             left = helper(exp[:i])
        #             right = helper(exp[i+1:])
        #             for l in left:
        #                 for r in right:
        #                     if exp[i] == "*":
        #                         res.append(l * r)
        #                     if exp[i] == "-":
        #                         res.append(l - r)
        #                     if exp[i] == "+":
        #                         res.append(l + r)
        #     return res
       
        # return  helper(expression)
        #TC O(N^3) SC O(N)
        # n = len(expression)
        # memo = {}
        # def helper(exp):
        #     if exp in memo:
        #         return memo[exp]
        #     res = []
        #     if exp.isdigit():
        #         return [int(exp)]
        #     for i in range(len(exp)):
        #         if exp[i] in "+-*":
        #             left = helper(exp[:i])
        #             right = helper(exp[i+1:])
        #             memo[exp] = res
        #             for l in left:
        #                 for r in right:
        #                     if exp[i] == "*":
        #                         res.append(l * r)
        #                     if exp[i] == "-":
        #                         res.append(l - r)
        #                     if exp[i] == "+":
        #                         res.append(l + r)
        #     return res
       
        # return  helper(expression)
        #TC O(N^2) SC O(N)
        n = len(expression)
        memo = {}
        def helper(start,end):
            if (start,end) in memo:
                return memo[(start,end)]
            exp = expression[start:end+1]
            res = []
            if exp.isdigit():
                return [int(exp)]
            for i in range(start,end):
                if expression[i] in "+-*":
                    left = helper(start,i-1)
                    right = helper(i+1,end)
                    for l in left:
                        for r in right:
                            if expression[i] == "*":
                                res.append(l * r)
                            if expression[i] == "-":
                                res.append(l - r)
                            if expression[i] == "+":
                                res.append(l + r)
            memo[(start,end)] = res
            return res
       
        return  helper(0,n-1)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap ={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        def helper(i,path):
            if len(path) == len(digits):
                result.append(path)
                return 
            for j in hashmap[digits[i]]:
                helper(i+1,path+j)
        helper(0,"")
        return result

        
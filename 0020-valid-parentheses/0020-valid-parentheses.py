class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        match = {'(':')','{':'}','[':']'}
        for i in s:
            if i in match:
                stack.append(i)
            elif len(stack)==0 or i !=match[stack.pop()]:
                return False
        #  return True
        
        return len(stack) == 0
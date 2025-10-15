class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashset = set(wordDict)
        memo = [0] *len(s)
        def helper(pivot):
            if pivot == len(s):
                return True
            if memo[pivot] == 1:
                return False
            for i in range(pivot,len(s)):
                sub = s[pivot:i+1]
                if sub in hashset:
                    if helper(i+1):
                        return True
            memo[pivot] = 1
            return False
        return helper(0)


        
        
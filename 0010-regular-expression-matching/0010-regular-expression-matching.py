class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #TC O(2^(N+M)) OC (N+M)
        # n = len(s)
        # m = len(p)
        # def helper(i,j):
        #     if i == n and j== m:
        #         return True
        #     if j == m:
        #         return False
        #     if j + 1 < m and p[j+1] == "*":
        #         if  i < n and (s[i] == p[j] or p[j] == "."): 
        #            return  helper(i+1,j) or helper(i,j+2)
        #         else:
        #            return  helper(i,j+2)
        #     elif i < n and ( s[i] == p[j] or p[j] == "." ):
        #        return  helper(i+1,j+1)
        #     return False
        # return helper(0,0) 
        #TC O(N*M) SC O(N+M)
        m = len(p)
        n = len(s)
        memo = {}
        def helper(i,j):
            if i == n and j == m:
                return True
            if j == m:
                return False
            if (i,j) in memo:
                return  memo[(i, j)]
            if j + 1 < m and p[j+1] == "*":
                if i < n and (s[i] == p[j] or p[j] == "."):
                    memo[(i, j)] = helper(i+1,j) or helper(i,j+2) 
                else:
                    memo[(i, j)] = helper(i,j+2)  
            elif i < n and( s[i] == p[j] or p[j] == "."):
                memo[(i, j)] = helper(i+1,j+1)
            else:
                memo[(i, j)] = False
                
            return  memo[(i, j)]
        return helper(0,0)
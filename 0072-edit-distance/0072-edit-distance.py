class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        memo = {}
        def dfs(i,j):
            if i == n:
                return m - j
            if j == m:
                return n - i
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i] == word2[j]:
                res = dfs(i+1,j+1)
            else:
                dele = 1 + dfs(i,j+1)
                edit = 1 + dfs(i+1,j+1)
                add = 1 + dfs(i+1,j)
                res = min(dele,add,edit)
                memo[(i,j)] = res
            return res
        return dfs(0,0)
            
        
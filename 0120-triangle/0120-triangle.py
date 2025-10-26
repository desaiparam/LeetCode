class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}
        def helper(i,j):
            if i == n-1:
                return triangle[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            total = triangle[i][j] + min(helper(i+1,j), helper(i+1,j+1))
            memo[(i,j)] = total
            return total
        return helper(0,0)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memoisation = {}
        def helper(i,j):
            if i == 0 or j == 0:
                return 1
            if i < 0  or j < 0:
                return 0
            if (i,j)in  memoisation:
                return memoisation[(i,j)]
            case0 = helper(i,j-1)
            case1 = helper(i-1,j)
            memoisation[(i,j)] = case0 + case1
            return memoisation[(i,j)]
        return helper(m-1,n-1)
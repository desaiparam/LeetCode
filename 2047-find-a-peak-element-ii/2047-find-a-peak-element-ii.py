class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def findMax(mat,n,m,mid):
            maxVal = -1
            index = -1
            for i in range(n):
                if mat[i][mid] > maxVal:
                    maxVal = mat[i][mid]
                    index = i
            return index
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1

        while low <= high:
            mid = (low + high) // 2
            row = findMax(mat,n,m,mid)
            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < m else -1
            if mat[row][mid] > left and mat[row][mid] > right:
                return [row,mid]
            elif mat[row][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        return [-1,-1]





        
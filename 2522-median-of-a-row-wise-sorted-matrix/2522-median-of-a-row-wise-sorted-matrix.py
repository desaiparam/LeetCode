class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        def upperbound(matVal,target,n):
            low = 0
            high = n -1
            while low <= high:
                mid = (low + high) //2
                if matVal[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            return low
        def blackbox(grid,n,m,mid):
            count = 0
            for i in range(n):
                count += upperbound(grid[i],mid,m)
            return count

        n = len(grid)
        m = len(grid[0])
        low = min(row[0] for row in grid)
        high = max(row[-1] for row in grid)
        req = (n * m)// 2
        while low <= high:
            mid = (low+high)//2
            smaller = blackbox(grid,n,m,mid)
            if smaller <= req:
                low = mid +1
            else:
                high = mid - 1
        return low

        
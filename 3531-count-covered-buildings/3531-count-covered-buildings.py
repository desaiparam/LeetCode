class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xmap = {}
        ymap = {}
        for x,y in buildings:
            if x not in xmap:
                xmap[x] = []
            xmap[x].append(y)
            if y not in ymap:
                ymap[y] = []
            ymap[y].append(x)
        ans = 0
        rowmax = {}
        rowmin = {}
        colmin = {}
        colmax = {}
        for x in xmap:
            rowmin[x] = min(xmap[x])
            rowmax[x] = max(xmap[x])
        for y in ymap:
            colmin[y] = min(ymap[y])
            colmax[y] = max(ymap[y])
        for x,y in buildings:
            if rowmin[x] < y < rowmax[x] and colmin[y] < x <colmax[y]:
                ans += 1
        return ans

        
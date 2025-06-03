class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        print(points)
        arrow = 1
        arrow_pos = points[0][1]
        for start,end in points[1:]:
            if start > arrow_pos:
                arrow += 1
                arrow_pos = end
        return arrow

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        result = [intervals[0]]
        for start,end in intervals[1:]:
            outTime = result[-1][1]
            if outTime >= start:
                result[-1][1] = max(outTime,end)
            else:
                result.append([start,end])
        return result
            

        
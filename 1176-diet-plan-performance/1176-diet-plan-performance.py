class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        i = 0
        j = k-1
        n = len(calories)
        windowsum = sum(calories[0:k])
        points = 0
        while j < n:
            if windowsum < lower:
                points -=1
            if windowsum > upper:
                points += 1
            windowsum -= calories[i]
            i += 1
            j += 1
            if j < n:
                windowsum += calories[j]
        return points


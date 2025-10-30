class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        higher = 0
        for i in range(n-1,-1,-1):
            if higher <= temperatures[i]:
                higher = temperatures[i]
                continue
            day = 1
            while temperatures[day+i] <= temperatures[i]:
                # print(temperatures[day+i])
                day += result[day+i]
            result[i] = day
        return result
            


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        yr = [0] * (2051)
        for log in logs:
            birt = log[0] - 1950  # Birth year
            deat = log[1] - 1950 # Death year
    
    # Increment population for each year the person is alive
            for year in range(birt, deat):  # From birth to the year before death
                yr[year] += 1
        print(yr)
        max_pop = 0
        max_id = 0
        for idx , ytr in enumerate(yr):
            if ytr > max_pop:
                max_pop = ytr
                max_id = idx
        return max_id + 1950

        
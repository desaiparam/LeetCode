class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        def calculateDays(weights,cap):
            days = 1
            load = 0
            for i in weights:
                if load+i > cap:
                    days+=1
                    load = i
                else:
                    load+=i
            return days

        while low <= high:
            mid = (low+high)//2
            daysNumber = calculateDays(weights,mid)
            if daysNumber <= days:
                high = mid- 1
            else:
                low = mid + 1
        return low
    
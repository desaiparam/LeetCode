class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def poss(nums,day,m,k):
            count = 0
            NumberOfBouquets = 0
            for i in range(len(nums)):
                # print(nums[i])
                # print("day",day)
                if nums[i] <= day:
                    count += 1
                else:
                    NumberOfBouquets += count//k
                    # print(NumberOfBouquets)
                    count = 0
            NumberOfBouquets += count//k
            if NumberOfBouquets >= m:
                return True
            else:
                return False
        # miny = min(bloomDay)
        # maxy = max(bloomDay)
        # for i in range(miny,maxy+1):
        #     print(i)
        #     if poss(bloomDay,i,m,k) == True:
        #         return i 
        low = min(bloomDay)
        high = max(bloomDay)
        ans = high
        while low <= high:
            mid = (low+high) // 2
            if poss(bloomDay,mid,m,k) == True:
                ans  = mid
                high = mid -1
            else:
                low = mid + 1
        return low
        

        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        # total = 0
        while left <= right:
            mid = (left + right) // 2
            # print(mid for pile in piles)
            # for i in piles:
            #     total += (i + mid - 1)//mid
            total = sum((i + mid - 1)// mid for i in piles)
            print(total)
            if total > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
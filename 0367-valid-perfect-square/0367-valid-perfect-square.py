class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = (left + right) //2
            print(mid)
            if mid * mid == num:
                return True
            elif mid * mid < num :
                left = mid + 1
            elif mid * mid > num :
                right = mid - 1
        return False

        
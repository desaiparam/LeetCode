class Solution:
    def maxA(self, n: int) -> int:
        if n <= 6:
            return n
        if n in {7,11,15}:
            return 3 * self.maxA(n-4)
        return 4 * self.maxA(n-5)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        ldividend = abs(dividend)
        ldivisor = abs(divisor)

        res = 0
        while ldividend >= ldivisor:
            numshifts = 1
            while (ldivisor << numshifts) <= ldividend:
                numshifts += 1
            numshifts -= 1
            res += 1 << numshifts
            ldividend -= ldivisor << numshifts
        if dividend < 0 and divisor < 0:
            return res
        if dividend < 0 or divisor < 0:
            return -res
        return res


        
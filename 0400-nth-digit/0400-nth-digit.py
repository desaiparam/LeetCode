class Solution:
    def findNthDigit(self, n: int) -> int:
        # digits = [0] * 100
        # digits[-1] = 1 
        # result = ""
        
        # while len(result) < n:
        #     num_str = ''.join(map(str, digits)).lstrip('0') or '0'
        #     result += num_str
        #     idx = len(digits) - 1
        #     while idx >= 0:
        #         if digits[idx] == 9:
        #             digits[idx] = 0
        #             idx -= 1
        #         else:
        #             digits[idx] += 1
        #             break
        # return int(result[n - 1])
        length = 1
        count = 9
        start = 1
        while n > length*count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        number = start + (n-1)//length
        digit_index = (n-1) % length
        return int(str(number)[digit_index])

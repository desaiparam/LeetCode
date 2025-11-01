class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = []
        carry = 1
        i = n - 1
        # for i in range(len(digits)-1,-1,-1):
        #     print(digits[i])
        while i >= 0 or carry:
            newA = digits[i] + carry
            carry = newA //10
            digits[i] = newA % 10
            res.append(digits[i])
            print(newA,carry,res)
            i -= 1
        res.reverse()
        return res



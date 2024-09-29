class Solution:
    sys.set_int_max_str_digits(100000000) 
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = reduce(lambda x, y: x * 10 + y, num)
        print(num)
        newInt = num+k
        ans = [int(dig) for dig in str(newInt)]
        return ans
        
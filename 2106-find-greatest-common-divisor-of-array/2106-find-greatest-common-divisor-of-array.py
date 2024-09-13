import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        nums.sort()
        print(nums)
        smaller=nums[0]
        larger=nums[-1]
        print("Larger:", larger)
        print("Smaller:", smaller)
        return math.gcd(smaller,larger)

      
import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smaller = float('inf')
        larger = float('-inf')
        # gcf=0
        for i in range(len(nums)):
            if smaller > nums[i]:
                smaller = nums[i]
                print("Smaller:", smaller)
            if larger < nums[i]:
                larger = nums[i]
                print("Larger:", larger)
        if smaller!=float('inf') and larger!=float('-inf') :
            return math.gcd(smaller,larger)
        return 1 


      
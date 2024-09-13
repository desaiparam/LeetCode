import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        #SOLUTION 1
        # smaller = float('inf')
        # larger = float('-inf')
        # # gcf=0
        # for i in range(len(nums)):
        #     if smaller > nums[i]:
        #         smaller = nums[i]
        #         print("Larger:", larger)
        #     if larger < nums[i]:
        #         larger = nums[i]
        #         print("Larger:", larger)
        # if smaller!=float('inf') and larger!=float('-inf') :
        #     return math.gcd(smaller,larger)
        # return 1 

        #Solution 2
        nums.sort()
        print(nums)
        smaller=nums[0]
        larger=nums[-1]
        print("Larger:", larger)
        print("Smaller:", smaller)
        return math.gcd(smaller,larger)
        # return 1


      
import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # smaller = float('inf')
        # larger = float('-inf')
        # gcf=0
        # for i in range(len(nums)):
        #     # print(nums[i])
        #     if(smaller>nums[i]):
        #         smaller = nums[i]
        #         print("Smaller:", smaller)
        #     elif(larger<nums[i]):
        #         larger = nums[i]
        #         print("Larger:", larger)
        #     if(smaller!=float('inf') and larger!=float('inf')):
        #         return math.gcd(smaller,larger)
        # return 1 
        smaller = float('inf')
        larger = float('-inf')

        for i in range(len(nums)):
            if nums[i] < smaller:
                smaller = nums[i]
                print("Smaller:", smaller)
            if nums[i] > larger:
                larger = nums[i]
                print("Larger:", larger)

        # Compute the GCD only if smaller and larger are valid integers
        if smaller != float('inf') and larger != float('-inf'):
            return math.gcd(smaller, larger)
            print("GCD of smaller and larger:", gcf)
        else:
            return 1
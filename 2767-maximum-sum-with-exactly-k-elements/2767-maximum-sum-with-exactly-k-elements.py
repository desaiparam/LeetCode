class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        #SOLUTION 1
        # maxi = max(nums)
        # nums.remove(maxi)
        # sumy = 0
        # while k > 0:
        #     sumy += maxi
        #     nums.append(maxi+1)
        #     maxi = max(nums)
        #     nums.remove(maxi)
        #     k-=1
        # return sumy
        #SOLUTION 2
        return max(nums)*k + (k*(k-1))//2
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        nums.remove(maxi)
        sumy = 0
        while k > 0:
            sumy += maxi
            nums.append(maxi+1)
            maxi = max(nums)
            nums.remove(maxi)
            k-=1
        return sumy
        
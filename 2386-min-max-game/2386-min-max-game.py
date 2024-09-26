class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            n = len(nums)
            newNums = []
            for i in range(0,n,2):
                a = nums[i]
                b = nums[i+1]
                half = i//2
                if half % 2 == 0 :
                    newNums.append(min(a,b))        
                else:
                    newNums.append(max(a,b))
                # print(newNums)
            nums = newNums
        return nums[0]
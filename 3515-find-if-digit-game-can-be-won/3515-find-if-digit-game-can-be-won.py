class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        A = []
        B = []
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] > 9:
                A.append(nums[i])
            else:
                B.append(nums[i])
        total_A = sum(A)
        total_B = sum(B)
        if total_A == total_B:
            return False
       
        return True
        
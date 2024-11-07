class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # l_s = 0
        # for i in range(len(nums)):
        #     c =0
        #     for j in range(i,len(nums)):
        #         if c == 2:
        #             break
        #         if nums[j] == 0:
        #             c += 1
        #         if c <= 1:
        #             l_s = max(l_s,j-i+1)
        # return l_s
        i =0
        j =0
        c = 0
        l_s = -1
        while j < len(nums):
            if nums[j] == 0:
                c += 1
            while c >= 2:
                if nums[i] == 0:
                    c -= 1
                i += 1
            l_s = max(l_s,(j-i+1))
            j += 1
        return l_s

        


        
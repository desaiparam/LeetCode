class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Solution 1
        # sets = {}
        # ans = []
        # for i in range(1,len(nums)+1):
        #     sets[i] = 0
        # for i in nums:
        #     sets[i] +=1
        # for key,val in sets.items():
        #     if val == 0:
        #         ans.append(key)
        # return ans
        #Solution 2
        sets = set(nums)
        ans = []
        for i in range(1,len(nums)+1):
            if i not in sets:
                ans.append(i)
        return ans
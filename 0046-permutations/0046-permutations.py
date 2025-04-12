class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #Solution 1
        # ans = []
        # freq = [False] * len(nums)
        # ds = []
        # def helper(nums,ds,ans,freq):
        #     if len(ds) == len(nums):
        #         ans.append(ds[:])
        #         return 
        #     for i in range(len(nums)):
        #         if not freq[i]:
        #             freq[i] = True
        #             ds.append(nums[i])
        #             helper(nums,ds,ans,freq)
        #             ds.pop()
        #             freq[i] = False
        # helper(nums,ds,ans,freq)
        # return ans

        #Solution 2
        ans = []
        def helper(index,nums,ans):
            if index == len(nums):
                # for i in nums:
                #     ans.append([i])
                ans.append(nums[:])
                return 
            for i in range(index,len(nums)):
                swap(i,index,nums)
                helper(index+1,nums,ans)
                swap(i,index,nums)
        def swap(i,j,nums):
            print("adsfg")
            nums[i],nums[j] = nums[j],nums[i]
        helper(0,nums,ans)
        return ans
        
        
        
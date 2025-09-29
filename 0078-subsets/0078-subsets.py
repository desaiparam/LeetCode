class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(path,idx):
            ans.append(path[:])
            for i in range(idx,len(nums)):
                path.append(nums[i])
                helper(path,i+1)
                path.pop()
        helper([],0)
        return ans

        
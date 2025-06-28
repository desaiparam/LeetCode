class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(i,arr,target):
            # if i == len(candidates):
            if 0 == target:
                ans.append(arr[:])
                return
            if i == len(candidates) or target<0:
                return
            arr.append(candidates[i])
            helper(i,arr,target-candidates[i])
            arr.pop()
            helper(i+1,arr,target)
        helper(0,[],target)
        return ans
            
            
        
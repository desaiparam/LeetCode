class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def helper(i,arr,target):
            if target == 0:
                ans.append(arr[:])
                return
            for indx in range(i,len(candidates)):
                if indx > i  and candidates[indx] == candidates[indx-1]:
                    continue
                if candidates[i] > target:
                    break
                arr.append(candidates[indx])
                helper(indx+1,arr,target-candidates[indx])  
                arr.pop()
        helper(0,[],target)
        return ans
        
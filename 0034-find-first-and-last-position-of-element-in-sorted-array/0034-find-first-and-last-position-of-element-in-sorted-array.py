class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerbound(nums,n,x):
            low = 0
            high = n-1
            ans = n
            while low <= high:
                mid = (low+high)//2
                if nums[mid] >= x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            print(ans)
            return ans

        def upperbound(nums,n,x):
            low = 0
            high = n-1
            ans = n
            print(n)
            while low <= high:
                mid = (low+high)//2
                if nums[mid] > x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            print(ans)
            return ans
        lb = lowerbound(nums,len(nums),target)
        if lb == len(nums) or nums[lb] != target:
            return [-1,-1]
        ub = upperbound(nums,len(nums),target)
        return [lb,(ub -1)]


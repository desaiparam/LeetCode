class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # left = 0
        # right = len(nums) - 1
        # mid = len(nums)//2
        # while left < right:
        #     if nums[left] == pivot :
        #         nums[left] , nums[mid] = nums[mid] , nums[left]
        #     elif nums[right] == pivot :
        #         nums[right] , nums[mid] = nums[mid] , nums[right]
        #     elif nums[left] < nums[right]:
        #         nums[left] , nums[right] = nums[right] , nums[left]
        #     left += 1
           
        #     # print("fghb")
        #     print(nums) 

        ans = []
        left = []
        right = []
        for i in nums:
            if i < pivot:
                ans.append(i)
                # print("ans",ans)
            elif i > pivot:
                right.append(i)
                # print("right",right)
            else:
                left.append(i)
                # print("left",left)
        ans.extend(left)
        ans.extend(right)
        return ans
            
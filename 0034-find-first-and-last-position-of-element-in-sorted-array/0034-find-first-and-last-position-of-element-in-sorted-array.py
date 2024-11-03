class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        while left <= right:
            mid = left + ((right - left) // 2)
            # if nums[mid] == target:
            #     # rigth = mid - 1
            #     # print(nums[mid])
            #     break
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        ans.append(left)
        left2 = left
        right2 = len(nums) - 1
        while left2 <= right2:
            mid2 = left2 + ((right2 - left2) // 2)
            # if nums[mid2] == target and nums[mid2] == left:
            #     # rigth = mid2 - 1
            #     # print("5120",nums[mid2])
            #     break
            if nums[mid2] <= target:
                # print("right123445",right2)
                left2 = mid2 + 1
            else:
                # print("left123456",left2)
                right2 = mid2 - 1
            print("mid2",mid2)
            print("right",right2)
            print("left",left2)
        ans.append(right2)

        print(ans)
        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        return ans
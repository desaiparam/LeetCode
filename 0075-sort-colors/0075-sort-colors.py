from collections import deque
from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #Solution 1 easy sorting TC :O(nlogn) SC : O(n)
        # nums.sort()

        #Solution 2 using stack O(n) O(n)
        # stack = deque()
        # count_2 = 0
        # for i in range(len(nums)):
        #     if nums[i] == 2:
        #         count_2 += 1
        # print(count_2)
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         stack.append(nums[i])
        #     if nums[i] == 0:
        #         stack.appendleft(nums[i])
        #     print(stack)
        # for i in range(len(nums)):
        #     if i < count_2:
        #         stack.append(2)
        #     else:
        #         stack.append
        # print(list(stack))
        # nums[:] = list(stack)

        #Solution 3 using sets TC O(n) SC O(1)
        # sets = {}
        # sets = defaultdict(int)
        # if len(nums) <= 1:
        #     return nums
        # for i in range(len(nums)):
        #     if nums[i] in sets:
        #         sets[nums[i]] += 1
        #     else:
        #         sets[nums[i]] = 1
        # for i in range(len(nums)):
        #     if i < sets[0]:
        #         nums[i] = 0
        #     elif i < sets[1] + sets[0]:
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2
        #Solution 4 Dutch National Flag Alogrith
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                # low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[high],nums[mid] = nums[mid],nums[high]
                high -= 1
                # mid += 1
        



        """
        Do not return anything, modify nums in-place instead.
        """
        
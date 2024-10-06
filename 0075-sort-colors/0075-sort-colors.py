from collections import deque
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #Solution 1 easy sorting
        # nums.sort()

        #Solution 2 using stack
        stack = deque()
        count_2 = 0
        for i in range(len(nums)):
            if nums[i] == 2:
                count_2 += 1
        print(count_2)
        for i in range(len(nums)):
            if nums[i] == 1:
                stack.append(nums[i])
            if nums[i] == 0:
                stack.appendleft(nums[i])
            print(stack)
        for i in range(len(nums)):
            if i < count_2:
                stack.append(2)
            else:
                stack.append
        print(list(stack))
        nums[:] = list(stack)

        """
        Do not return anything, modify nums in-place instead.
        """
        
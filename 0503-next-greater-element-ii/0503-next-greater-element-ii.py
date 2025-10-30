class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1] * n
        for i in range(0,2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                result[stack.pop()] = nums[i%n]
            if  stack and i %n == stack[-1]:
                break
            if i < n:
                stack.append(i)
        return result
 
        
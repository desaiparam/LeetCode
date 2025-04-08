class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = len(nums)//2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        return self.merge(left,right)
    def merge(self,left:List[int],right:List[int]):
        left_pointer = 0
        right_pointer = 0
        result = []
        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer] < right[right_pointer]:
                result.append(left[left_pointer])
                left_pointer += 1
            else:
                result.append(right[right_pointer])
                right_pointer += 1
        result.extend(left[left_pointer:])
        result.extend(right[right_pointer:])
        return result

        
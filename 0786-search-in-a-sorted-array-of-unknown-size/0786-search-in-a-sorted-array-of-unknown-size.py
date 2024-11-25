# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # print(reader)
        # for i in range(len(reader)):
        #     print(reader.get(i))
        nums = []
        # nums.append(reader)
        # print(nums)
        i = 0
        while reader.get(i) != 2147483647:
            print(reader.get(i))
            nums.append(reader.get(i))
            i += 1
        print(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(nums[mid])
            if nums[mid] == target:
                print("mid",mid)
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right -= 1
        return  -1
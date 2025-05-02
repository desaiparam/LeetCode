class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge Sort
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
    # #Quick sort(this wont work as TC for test case 11 is O(n^2))
    #     # print("waesdfgh")
    #     self.quick(nums,0,len(nums) - 1)
    #     return nums
    # def quick(self,nums:List[int],low:int,high:int):
    #     if low < high:
    #         # print(low,"low")
    #         # print(high,"high")
    #         partitionIndex = self.partition(nums,low,high)
    #         self.quick(nums,partitionIndex+1,high)
    #         self.quick(nums,low,partitionIndex-1)
    # def partition(self,nums:List[int],low:int,high:int):
    #     # print("Sdfgh")
    #     i = low
    #     j = high
    #     pivot = nums[low]
    #     while i < j:
    #         while nums[i] <= pivot and i <= high -1:
    #             i+=1
    #         while nums[j] > pivot and j >= low+ 1:
    #             j-=1
    #         if i < j:
    #             nums[i],nums[j] = nums[j],nums[i]

    #     nums[low],nums[j] = nums[j],nums[low]
    #     return j



        
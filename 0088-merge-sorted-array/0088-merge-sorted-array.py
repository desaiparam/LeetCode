class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-1,-1,-1):
            print(len(nums1))
            if nums1[i] == 0 and len(nums1)>m:
                nums1.pop(i)
            else:
                break
        nums1.extend(nums2)
        print(nums1)
        nums1.sort()
        print(nums1)
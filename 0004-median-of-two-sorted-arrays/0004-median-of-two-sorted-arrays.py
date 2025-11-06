class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        n1 = len(nums1)
        n2 = len(nums2)
        low = 0
        high = n1 
        while low <= high:
            midn1 = low + (high - low)//2
            midn2 = (n1+n2)//2 - midn1
            leftn1 = float('-inf') if midn1 == 0 else nums1[midn1 -1]
            rightn1 = float('inf') if midn1 == n1 else nums1[midn1]
            leftn2 = float('-inf') if midn2 == 0 else nums2[midn2 -1]
            rightn2 = float('inf') if midn2 == n2 else nums2[midn2]

            if leftn1 <= rightn2 and rightn1 >= leftn2:
                if (n1+n2) % 2 != 0:
                    return min(rightn1,rightn2)
                return (max(leftn1,leftn2) + min(rightn1,rightn2))/2
            elif leftn1 > rightn2:
                high = midn1
            else:
                low = midn1 + 1

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        sets = set(nums1)
        arr = []
        if 0 in sets:
            return 0
        if len(nums1) == 1 and len(nums2) == 0:
            return float(nums1[0])
       
            # print("sdfg")
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        arr.extend(nums1[i:])
        arr.extend(nums2[j:])
        print(arr)
        res = 0 
        if len(arr) % 2 != 0:
            mid = (len(arr) + 1) // 2
            # mid = len(arr) // 2
            # print(arr[mid]) 
            res = arr[mid-1]
        elif len(arr) % 2 == 0:
            mid = len(arr) // 2
            print(mid)
            res = (arr[mid] + arr[mid - 1]) / 2
            # print(arr[mid]) 
            # res = ((len(arr)/2)+(len(arr)/2)+1 )/2
            # if res != 
        return res
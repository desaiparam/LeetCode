class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2 , nums1
        n1 = len(nums1)
        n2 = len(nums2)
        le = 0
        re = n1
        while le <= re:
            p1 = (le + re) //2
            p2 = (n1 + n2 + 1) //2 - p1

            l1 = float('-inf') if p1 == 0 else nums1[p1-1]
            r1 = float('inf') if p1 == n1 else nums1[p1]

            l2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            r2 = float('inf') if p2 == n2 else nums2[p2]

            if l2 <= r1 and l1 <= r2:
                if (n1 + n2) % 2 != 0:
                    return max(l1,l2)
                return (max(l1,l2) + min(r1,r2)) /2
            elif l1 > r2:
                re = p1 - 1
            else:
                le = p1 + 1
        
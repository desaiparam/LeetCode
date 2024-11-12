class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            ans =[]
            ma = Counter(nums1)
            for i in nums2:
                if i in ma and ma[i] > 0:
                    ans.append(i)

                    ma[i] -=1
            return ans
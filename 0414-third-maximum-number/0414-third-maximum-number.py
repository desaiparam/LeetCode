import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sets = list(set(nums))
        sets.sort(reverse = True)
        print(sets)

        if len(sets) >= 3:
            return sets[2]
        else:
            return max(sets)
        return 0

        
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def helper(target):
            tr = 0
            br = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1 
                if tops[i] == target and bottoms[i] == target:
                    continue
                if tops[i] != target:
                    tr += 1
                if bottoms[i] != target:
                    br += 1
            return min(tr,br)
        res = helper(tops[0])
        if res != -1:
            return res
        return helper(bottoms[0])
        
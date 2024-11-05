class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorHeight = sorted(heights)
        print(sorHeight)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorHeight[i]:
                count += 1
        return count
        
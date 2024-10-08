class Solution:
    def maxArea(self, height: List[int]) -> int:
        area =0
        right = len(height)-1
        left = 0
        while left<right:
            area= max(area,(right-left) *min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area

        
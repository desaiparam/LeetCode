class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n -1
        area = 0
        while left < right:
            if height[left] <= height[right]:
                area = max(area,min(height[left],height[right]) * (right-left))
                print(area)
                left += 1
            else:
                area = max(area,min(height[right],height[left]) * (right-left))
                right -= 1
        return area

        
         
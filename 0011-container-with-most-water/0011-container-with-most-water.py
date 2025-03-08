class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0 
        while left < right:
            # print("area",area)
            area = max(area,(right - left) * min(height[left],height[right]))
            # print("right",right)
            # print("left",left)
            # print("height[right]",height[right])
            # print("height[left]",height[left])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        # print(area)
        
        return area


        
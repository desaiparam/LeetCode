class Solution:
    def trap(self, height: List[int]) -> int:
        n =len(height)
        left = 0
        right = n - 1
        leftHeight = height[left]
        rightHeight = height[right]
        counter = 0
        while left < right:
            if leftHeight < rightHeight:
                left += 1
                leftHeight = max(leftHeight,height[left])
                counter += leftHeight - height[left]
            else:
                right -= 1
                rightHeight = max(rightHeight,height[right])
                counter += rightHeight - height[right]
        return counter

        
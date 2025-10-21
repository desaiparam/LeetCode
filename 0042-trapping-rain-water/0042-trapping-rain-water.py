class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        lw = height[left]
        rw = height[right]
        result = 0
        while left < right:
            if lw < rw:
                left += 1
                lw = max(lw,height[left])
                result += lw  - height[left]
            else:
                right -= 1
                rw = max(rw,height[right])
                result += rw  - height[right]
        return result
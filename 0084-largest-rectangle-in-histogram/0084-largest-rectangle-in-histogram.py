class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        minHeigt= float('inf')
        i = 0
        stack = []
        area = 0
        while i < n:
            while stack  and heights[stack[-1]] > heights[i]:
                prevVal = stack.pop() 
                width = i - stack[-1] -1 if stack else i 
                newArea = heights[prevVal] * width
                print(newArea,width,heights[prevVal])
                area = max(area,newArea)
            stack.append(i)
            i += 1
        while stack:
            prevVal = stack.pop() 
            width = i - stack[-1] -1 if stack else i
            newArea = heights[prevVal] * width
            print(newArea,width,heights[prevVal])
            area = max(area,newArea)
        return area

        
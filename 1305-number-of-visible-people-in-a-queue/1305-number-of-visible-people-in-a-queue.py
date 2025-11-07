class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n  = len(heights)
        ans = [0] * n
        stack = []
        i = 0
        while i < n:
            while stack and heights[stack[-1]] < heights[i]:
                # print(stack)
                indx = stack.pop()
                ans[indx] += 1
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)
            i += 1
        return ans

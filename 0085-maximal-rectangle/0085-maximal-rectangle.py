class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        preCal = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    # print(preCal,preCal[i-1][j] )
                    preCal[i][j] = 1+preCal[i-1][j] 
        print(preCal)
        area = 0
        for i in range(n):
            stack = []
            for j in range(m):
                while stack and preCal[i][stack[-1]] > preCal[i][j]:
                    preVal = stack.pop()
                    width = j - stack[-1] - 1 if stack else j
                    newArea = preCal[i][preVal] * width
                    area = max(area,newArea)
                stack.append(j)

            while stack:
                preVal = stack.pop()
                width = m - stack[-1] - 1 if stack else m
                newArea = preCal[i][preVal] * width
                area = max(area,newArea)
        return area

            
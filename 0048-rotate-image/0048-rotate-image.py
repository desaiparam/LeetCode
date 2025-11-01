class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1 2 3
        # 4 5 6
        # 7 8 9

        # After transpose
        # 1 7 4
        # 2 5 8
        # 3 6 9 
        # After rotation 
        # 7 4 1 
        # 8 5 2
        # 9 6 3
        for i in range(len(matrix)-1):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
        

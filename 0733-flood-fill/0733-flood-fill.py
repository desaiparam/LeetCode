class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og = image[sr][sc]
        if og == color:
            return image
        def dfs(i,j):
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == og:
                image[i][j] = color
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1) 
        dfs(sr,sc)
        return image

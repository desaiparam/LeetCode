class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            return [list(reversed(row)) for row in list(zip(*mat))]
        rotated = rotate(mat)
        for _ in range(4):
                if rotated == target:
                    return True
                rotated=rotate(rotated)
        return False        
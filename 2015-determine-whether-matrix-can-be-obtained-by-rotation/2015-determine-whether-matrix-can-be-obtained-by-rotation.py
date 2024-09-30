class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            transpo = list(zip(*mat))
            rotate = [list(reversed(row)) for row in transpo]
            return rotate
        rotated = rotate(mat)
        # Mn = len(rotated)
        # Mm = len(rotated[0])
        # Tn = len(target)
        # Tm = len(target[0])
        # if Mn == None or Tn == None or Mn == 0 or Tn == 0 or Mn != Tn or Mm != Tm:
        #     return False
        # else:
        for _ in range(4):
                if rotated == target:
                    return True
                rotated=rotate(rotated)
        return False        
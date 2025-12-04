class Solution:
    def countCollisions(self, directions: str) -> int:
        # seenR = 0
        # seenS = 0
        # collision = 0
        # for i in directions:
        #     if i == "R":
        #         seenR += 1
        #     elif i == "S":
        #         collision += seenR
        #         seenR = 0
        #         seenS = 1
        #     elif i == "L":
        #         if seenR > 0:
        #             collision += seenR + 1
        #             seenR = 0
        #             seenS = 1
        #         elif seenS == 1:
        #             collision += 1
        #             seenS = 1
                
        # return collision
        # THis MAKES SURE SO REMOVE THE EXTRA L and R on the sides
        directions = directions.lstrip('L').rstrip('R')
        # print(directions)
        return len(directions) - directions.count('S')
        
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        sets = set()
        for i , j in nums:
            for k in range(i,j+1):
                sets.add(k)
        return len(sets)
      
        

        
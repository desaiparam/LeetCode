class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # ans = [1]
        # pr = 1
        # for i in range(1,rowIndex+1):
        #     n_v = pr * (rowIndex - i + 1) //i
        #     ans.append(n_v)
        #     pr = n_v
        # return ans
        if rowIndex == 0:
            return [1]
        prevRow = self.getRow(rowIndex-1)
        row = [1]
        for i in range(1,rowIndex):
            row.append(prevRow[i-1]+prevRow[i])
        row.append(1)
        return row
            
            
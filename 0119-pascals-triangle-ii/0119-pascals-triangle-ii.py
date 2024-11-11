class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        pr = 1
        for i in range(1,rowIndex+1):
            n_v = pr * (rowIndex - i + 1) //i
            ans.append(n_v)
            pr = n_v
        return ans
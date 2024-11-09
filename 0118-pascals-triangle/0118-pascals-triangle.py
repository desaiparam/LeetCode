class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [1] * numRows
        if numRows == 0:
            return [[]]
        if numRows == 1:
            return [[1]]
        first = self.generate(numRows - 1)

        for i in range(1,numRows-1):
            ans[i] = first[-1][i-1] + first[-1][i]
        first.append(ans)

        return first

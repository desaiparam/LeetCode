class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        ans = []
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                sums = i + j
                d[sums].append(mat[i][j])
        print(d)
        for i in d.items():
            if i[0] % 2 == 0:
                print(i[1][::-1])
                ans.extend(i[1][::-1])
            else:
                print(i[1])
                ans.extend(i[1])
        return ans
        
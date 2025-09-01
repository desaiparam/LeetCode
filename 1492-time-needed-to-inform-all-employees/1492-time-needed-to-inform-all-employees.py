class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n <= 1:
            return 0
        subordinates = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                subordinates[manager[i]].append(i)
        def dfs(root):
            if not subordinates[root]:
                return 0
            maxy = 0
            for i in subordinates[root]:
                maxy = max(maxy,dfs(i))
            return maxy + informTime[root]
        return dfs(headID)

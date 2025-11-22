class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        discover = [-1] * n
        lowest = [0] * n
        maps = {i:[] for i in range(n)}
        self.time = 0
        res = []
        for u,v in connections:
            maps[u].append(v)
            maps[v].append(u)
        def helper(u,v):
            if discover[u] != -1:
                return 
            discover[u] = self.time
            lowest[u] = self.time
            self.time += 1
            for i in maps[u]:
                if i == v:
                    continue
                helper(i,u)
                if lowest[i] > discover[u]:
                    res.append([i,u])
                lowest[u] = min(lowest[u],lowest[i])
        helper(0,-1)
        return res

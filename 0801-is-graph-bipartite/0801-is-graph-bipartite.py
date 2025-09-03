class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [None] * n
        def dfs(u,c):
            color[u] = c
            for v in graph[u]:
                if color[v] is None:
                    if not dfs(v,1-c):
                        return False
                elif color[v] == c:
                    return False
            return True
        for i in range(n):
            if color[i] is None:
                if not dfs(i,0):
                    return False
        return True

        
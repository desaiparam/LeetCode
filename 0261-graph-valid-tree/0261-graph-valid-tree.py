class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph= [[] for _ in range(n)]
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for i in graph[node]:
                if i == parent:
                    continue
                if not dfs(i,node):
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(visited) == n

                

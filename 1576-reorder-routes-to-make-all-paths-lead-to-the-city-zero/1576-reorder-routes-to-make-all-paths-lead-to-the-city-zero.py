class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n
        edges = set()
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
            edges.add((i,j))
        print(graph)
        def dfs(root):
            visited[root] = True
            count = 0
            for i in graph[root]:
                if not visited[i]:
                    if (root,i) in edges:
                        count += 1
                    count += dfs(i)
            return count
        return dfs(0)
        
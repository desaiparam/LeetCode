class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n
        adj = [set() for _ in range(n)]
        for i,j in roads:
            deg[i] += 1
            deg[j] += 1
            adj[i].add(j)
            adj[j].add(i)
        best = 0
        for i in range(n):
            for j in range(i+1,n):
                rank = deg[i] + deg[j] - (1 if j in adj[i] else 0)
                if rank > best:
                    best = rank
        return best
        

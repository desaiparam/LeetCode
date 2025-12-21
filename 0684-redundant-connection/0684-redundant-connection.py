class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        def union(x,y):
            parentx = find(x)
            parenty = find(y)
            if parentx == parenty:
                return False
            parent[parenty] = parentx
            return True
        
        for x,y in edges:
            if not union(x,y):
                return [x,y]

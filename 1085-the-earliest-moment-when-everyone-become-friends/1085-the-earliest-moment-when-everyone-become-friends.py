class Disjoint:
    def __init__(self,users,n):
        self.parent = {i:i for i in users}
        self.rank = {i:0 for i in users}
        self.components = n
    def findParent(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    def unionByRank(self,u,v):
        ultiparentU = self.findParent(u)
        ultiparentV = self.findParent(v)
        if ultiparentU == ultiparentV:
            return 
        if self.rank[ultiparentU] < self.rank[ultiparentV]:
            self.parent[ultiparentV] = ultiparentU
        elif self.rank[ultiparentU] > self.rank[ultiparentV]:
            self.parent[ultiparentU] = ultiparentV
        else:
            self.parent[ultiparentU] = ultiparentV
            self.rank[ultiparentU] += 1
        self.components -= 1
        return True
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        users = set()
        for _,a,b in logs:
            users.add(a)
            users.add(b)
        uf = Disjoint(users,n)
        logs.sort(key=lambda x:x[0])
        for time,a,b in logs:
            uf.unionByRank(a,b)
            if uf.components == 1:
                return time
        return -1
        
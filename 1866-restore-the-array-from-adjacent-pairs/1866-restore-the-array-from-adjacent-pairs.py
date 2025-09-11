class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        start = None
        visited = set()
        res = []
        for i,j in adjacentPairs:
            adj_list[i].append(j)
            adj_list[j].append(i)
        for node in adj_list:
            if len(adj_list[node]) == 1:
                start = node
                break
        def dfs(node,prev):
            res.append(node)
            visited.add(node)
            for i in adj_list[node]:
                if i != prev:
                    dfs(i,node)
        dfs(start,None)
        return res
        
        
        
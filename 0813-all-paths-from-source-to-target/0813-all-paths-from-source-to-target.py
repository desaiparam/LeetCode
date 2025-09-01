class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        def dfs(root,path):
            if root == target:
                res.append(path)
                return 
            for i in graph[root]:
                dfs(i,path+[i])
        
        dfs(0,[0])
        return res

        
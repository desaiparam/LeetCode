class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
            #Solution 1 BFS TC:O(N^2) SC:O(N)
            # count = 0
            # n = len(isConnected)
            # vis = [False] * n
            # for i in range(n):
            #     if not vis[i]:
            #         q = deque([i])
            #         vis[i] = True
            #         count += 1
            #         while q:
            #             node = q.popleft()
            #             for ne in range(n):
            #                 if isConnected[node][ne] == 1 and not vis[ne]:
            #                     q.append(ne)
            #                     vis[ne] = True
            # return count
            vis = [False] * len(isConnected)
            def dfs(root):
                vis[root] = True
                for n in range(len(isConnected)):
                    if isConnected[root][n] ==1 and not vis[n]:
                        dfs(n)
            count = 0
            for i in range(len(isConnected)):
                if  not vis[i]:
                    dfs(i)
                    count += 1
            return count

            

        
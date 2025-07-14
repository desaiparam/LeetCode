class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
            count = 0
            n = len(isConnected)
            vis = [False] * n
            for i in range(n):
                if not vis[i]:
                    q = deque([i])
                    vis[i] = True
                    count += 1
                    print("q",q,"count",count)
                    while q:
                        node = q.popleft()
                        for ne in range(n):
                            if isConnected[node][ne] == 1 and not vis[ne]:
                                q.append(ne)
                                vis[ne] = True
            return count


        
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        visited[start] = True
        q = deque([start])
        while q:
            curr = q.popleft()
            if arr[curr] == 0:
                return True
            for i in (curr-arr[curr],curr+arr[curr]):
                if 0 <= i < len(arr) and not visited[i]:
                    visited[i] = True
                    q.append(i)
        return False

        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course,pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for i in adj[curr]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)
        print(ans)
        return ans if len(ans) == numCourses else []
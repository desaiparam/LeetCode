class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = deque([("(",1,0)])
        result = []
        while q:
            prev,openCount,closeCount = q.popleft()
            if openCount == n and closeCount == n:
                result.append(prev)
            if openCount < n:
                q.append((prev+"(",openCount+1,closeCount))
            if closeCount < openCount:
                q.append((prev+")",openCount,closeCount+1))
        return result

        
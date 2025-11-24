class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        q = deque([s])
        seen = set([s])
        found = False
        def isvalid(curr):
            count = 0
            for i in curr:
                if i.isalpha():
                    continue
                if i == "(":
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        while q and not found:
            for _ in range(len(q)):
                curr = q.popleft()
                if isvalid(curr):
                    res.append(curr)
                    found = True
                elif not found:
                    for i in range(len(curr)):
                        if curr[i].isalpha():
                            continue
                        baby = curr[:i] + curr[i+1:]
                        if baby not in seen:
                            q.append(baby)
                            seen.add(baby)
        return res

        
        
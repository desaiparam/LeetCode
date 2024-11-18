class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        # ds = set(deadends)
        # start = "0000"
        visi = set(deadends)
        que = deque()
        que.append(("0000",0))
        while que:
            lock , turns = que.popleft()
            if lock == target:
                return turns
            res = []
            for i in range(4):
                dig = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + dig + lock[i+1:])
                dig = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + dig + lock[i+1:])

            
            for j in res:
                if j not in visi:
                    visi.add(j)
                    que.append([j,turns+1])

    
        return -1











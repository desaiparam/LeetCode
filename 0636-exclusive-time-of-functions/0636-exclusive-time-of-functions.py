class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        prev = 0
        for i in logs:
            part = i.split(":")
            prId = int(part[0])
            prStatus = part[1]
            prTime = int(part[2])
            if prStatus == "start":
                if stack:
                    result[stack[-1]] +=  prTime - prev
                stack.append(prId)
            else:
                prTime += 1
                result[stack.pop()] += prTime - prev
            prev = prTime
        return result

        
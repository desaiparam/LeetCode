class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapy = {}
        for i in range(len(s)):
            mapy[s[i]] = i
        res = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end,mapy[s[i]])
            if i == end:
                res.append(end- start + 1)
                start = i + 1
        return res
         

        
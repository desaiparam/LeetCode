class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n
        x = {a for a,_ in trust}
        c = Counter(b for _,b in trust)
        for a , b in c.items():
            if b == n-1 and a not in x:
                return a
        return -1
    

        
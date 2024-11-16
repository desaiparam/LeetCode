class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = collections.defaultdict(list)
        for i in jewels:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        print(d)
        c = 0
        for i in stones:
            if i in d:
                c+=1
        print(c)
        return c
        
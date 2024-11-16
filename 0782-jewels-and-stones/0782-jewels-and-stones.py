class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        #SOLUTION 1 USING DEFAULTDICT
        # d = collections.defaultdict(list)
        # for i in jewels:
        #     if i not in d:
        #         d[i] = 1
        #     else:
        #         d[i] +=1
        # print(d)
        # c = 0
        # for i in stones:
        #     if i in d:
        #         c+=1
        # print(c)
        # return c
        #SOLUTION 2 USING SET
        d = set(jewels)
        c = 0
        for i in stones:
            if i in d:
                c +=1
        return c
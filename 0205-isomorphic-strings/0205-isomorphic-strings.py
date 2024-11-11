class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        # for i in s:
        #     if i in ds:
        #         ds[i] +=1
        #     else:
        #         ds[i] = 1
        # print("ds",ds)
        # for i in t:
        #     if i in dt:
        #         dt[i] +=1
        #     else:
        #         dt[i] = 1
        # print("dt",dt)
        
        # return Counter(ds.values()) == Counter(dt.values())
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]] = i
            if t[i] not in dt:
                dt[t[i]] = i
            if ds[s[i]] != dt[t[i]]:
                return False
        return True
        
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        res = set()
        seq = set()
        hashval = 0
        charm = {'A':1,'C':2,'G':3,'T':4}
        fac = 4**10
        for i in range(n):
            hashval = hashval* 4 + charm[s[i]]
            if i >= 10:
                hashval -= fac * charm[s[i-10]]
            if i >= 9:
                if hashval in seq:
                    res.add(s[i-9:i+1])
                else:
                    seq.add(hashval)
        return list(res)
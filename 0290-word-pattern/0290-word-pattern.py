class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern) != len(word):
            return False
        pW = {}
        wP = {}

        for p,w in zip(pattern,word):
            if pW.get(p) and pW[p] != w:
                return False
            if wP.get(w) and wP[w] != p:
                return False
            wP[w] = p
            pW[p] = w
        return True
        
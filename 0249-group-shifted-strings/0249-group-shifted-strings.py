class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = {}
        for i in strings:
            w = ()
            for c in range(len(i) - 1):
                ascii_diff = 26 + ord(i[c+1]) - ord(i[c])
                w += (ascii_diff % 26,)
            d[w] = d.get(w,[]) + [i]
        return list(d.values())




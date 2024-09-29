class Solution:
    def oddString(self, words: List[str]) -> str:
        n = len(words)
        m = len(words[0])
        diff = []
        for i in range(n):
            cur = []
            for j in range(m-1):
                cur.append(ord(words[i][j+1]) - ord(words[i][j]))
            diff.append(tuple(cur))
        c = collections.Counter(diff)
        for i in range(n):
            if c[diff[i]] == 1:
                return words[i]
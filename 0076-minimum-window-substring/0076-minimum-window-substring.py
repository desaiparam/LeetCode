class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tmap = Counter(t)
        left = 0
        miny = float('inf')
        smap = defaultdict(int)
        have = 0
        result = 0
        for i in range(len(s)):
            smap[s[i]] += 1
            if s[i] in tmap and smap[s[i]] == tmap[s[i]]:
                have += 1
            while have == len(tmap):
                if i - left + 1 < miny:
                    miny = i - left + 1
                    result = left
                smap[s[left]] -= 1
                if s[left] in tmap and smap[s[left]] < tmap[s[left]]:
                    have -= 1 
                left += 1
        return s[result:result+miny] if miny != float('inf') else ""
                


        
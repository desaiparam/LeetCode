class Solution:
    def alienOrder(self, words: List[str]) -> str:
        hashmap = defaultdict(set)
        ind = [0] * 26
        def buildgraph(words):
            for w in words:
                for i in w:
                    hashmap[i] = set()
            for i in range(len(words) - 1):
                f = words[i]
                s = words[i+1]
                if f.startswith(s) and len(f) > len(s):
                    hashmap.clear()
                    return 
                for j in range(min(len(f),len(s))):
                    fc = f[j]
                    sc = s[j]
                    if fc != sc:
                        if sc not in hashmap[fc]:
                            hashmap[fc].add(sc)
                            ind[ord(sc) - ord('a')] += 1
                        break
        buildgraph(words)
        if hashmap == 0:
            return ""
        sb = []
        q = deque()
        for i in hashmap.keys():
            if ind[ord(i) - ord('a')] == 0:
                q.append(i)
                sb.append(i)
        while q:
            curr = q.popleft()
            for i in hashmap[curr]:
                ind[ord(i)-ord('a')] -= 1
                if ind[ord(i) - ord('a')] == 0:
                    q.append(i)
                    sb.append(i)
        if len(sb) == len(hashmap):
            return ''.join(sb)
        return ""
        
        buildgraph(words)


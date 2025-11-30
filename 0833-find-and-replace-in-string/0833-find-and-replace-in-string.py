class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # hashmap = {idx:(src,tr) for idx,src,tr in zip(indices,sources,targets)}
        hashmap = {}
        for idx,src,tr in zip(indices,sources,targets):
            if s.startswith(src,idx):
                hashmap[idx] = (src,tr)
        res = ""
        i = 0
        n = len(s)
        while i < n:
            if i in hashmap:
                src,tr = hashmap[i]
                
                if s.startswith(src,i):
                    res += tr
                    i += len(src)
                    continue

            res += s[i]
            i += 1
        return res


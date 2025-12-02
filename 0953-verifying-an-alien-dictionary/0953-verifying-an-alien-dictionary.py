class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap= {}
        for i in range(len(order)):
            hashmap[order[i]] = i
        def notsorted(first,second):
            for i in range(min(len(first),len(second))):
                fc = first[i]
                sc = second[i]
                if fc != sc:
                    if hashmap[sc] > hashmap[fc]:
                        return False
                    else:
                        return True
            if len(first) > len(second):
                return True
            else:
                return False
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            if notsorted(first,second):
                return False
        return True

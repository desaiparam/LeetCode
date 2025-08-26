class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern) != len(word):
            return False
        pMap = {}
        wMap = {}
        print("word",word)
        for i in range(len(pattern)):
            if pattern[i] in pMap:
                if pMap[pattern[i]] != word[i]:
                    return False
            pMap[pattern[i]] = word[i]
            if word[i] in wMap:
                if wMap[word[i]] != pattern[i]:
                    return False
            wMap[word[i]] = pattern[i]
        return True
        
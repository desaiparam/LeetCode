class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        setS = {}
        setT = {}
        diff = 0
        for i in range(len(s)):
            setS[s[i]] = i
        print("setS",setS) 
        for j in range(len(t)):
            setT[t[j]] = j
        print("setT",setT) 
        for key in setS :
            if key in setT:
                diff += abs(setS[key] - setT[key])
        return diff

        
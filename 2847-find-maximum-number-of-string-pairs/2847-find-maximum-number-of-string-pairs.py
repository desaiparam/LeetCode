class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        sets = set()
        for i in words:
            if i in sets:
                count+=1
            else :
                sets.add(i[::-1])
        return count
        
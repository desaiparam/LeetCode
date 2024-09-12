class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        l= list(allowed)
        for word in words:
           if set(word).issubset(l):
            count+=1
        return count
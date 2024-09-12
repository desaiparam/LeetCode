class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        l= set(allowed)
        for word in words:
           for letter in word:
            if letter not in l:
                count+=1
                break
        return len(words)-count
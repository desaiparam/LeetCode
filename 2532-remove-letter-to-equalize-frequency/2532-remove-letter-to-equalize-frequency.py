class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            count = collections.Counter(word)
            count[word[i]] -=1
            if count[word[i]] == 0:
                del count[word[i]]
            if len(set(count.values())) ==1:
                return True
        return False 
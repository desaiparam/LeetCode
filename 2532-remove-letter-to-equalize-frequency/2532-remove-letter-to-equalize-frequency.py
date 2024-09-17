class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = collections.Counter(word)
        for i in word:
            count[i] -=1
            if count[i] == 0:
                del count[i]
            if len(set(count.values())) ==1:
                return True
            count[i]+=1
        return False 
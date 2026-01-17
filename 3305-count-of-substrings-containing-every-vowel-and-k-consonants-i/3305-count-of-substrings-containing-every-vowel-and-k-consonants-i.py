class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel = {'a':0,'e':0,'i':0,'o':0,'u':0}
        count = 0
        distinct = 0
        constant = 0
        j = 0
        for i in range(len(word)):
            if word[i] in vowel:
                vowel[word[i]]+=1
                if vowel[word[i]] ==1:
                    distinct += 1
            else:
                constant += 1
            while constant > k:
                if word[j] in vowel:
                    vowel[word[j]] -= 1
                    if vowel[word[j]] == 0:
                        distinct -= 1
                else:
                    constant -= 1
                j += 1
            if constant == k and distinct == 5:
                temp = j
                vowelcopy = vowel.copy()
                while temp <= i and word[temp] in vowelcopy and vowelcopy[word[temp]]>1:
                    vowelcopy[word[temp]] -= 1                
                    temp += 1
                count += (temp-j+1)
        return count

        

                
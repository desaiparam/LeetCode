class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        #bad question do not do it again just think of sliding window that the window will keep shifting from left to right you have to track the vowels in between with constants and they do not cross k limit the vowel map keeps track of how many time the frequency has been repeated and with help of that we determine the distinct vowels present with the constants present as well 
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

        

                